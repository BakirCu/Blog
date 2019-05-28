from errors import InputError
from configuration import Configuration
from data_base import UseDatabase
config_dict = Configuration.get_config()


class Book:
    def __init__(self, book, author, book_num):
        if not book or not author or not book_num:
            raise InputError(
                "Every positional argument: 'book', 'author', \
                    'book_num', must have some value")
        if not book.isalpha() or not author.isalpha():
            raise InputError('Book and author name must be alpha ')
        self.book = book
        self.author = author
        self.book_num = abs(int(book_num))

    @staticmethod
    def add_book(user):
        with UseDatabase(config_dict) as cursor:
            sql = '''INSERT INTO book(book, author, book_num)
                        VALUES(%s, %s, %s)
                        ON DUPLICATE KEY UPDATE \
                            book_num = VALUES(book_num) + book_num'''
            cursor.execute(sql, (user.book, user.author, user.book_num))

    @staticmethod
    def search_book_name(book_author_name_str):
        book_author_name = book_author_name_str.strip()
        if not book_author_name:
            raise InputError('Input must have some value')
        return book_author_name

    @staticmethod
    def search_book_database(book_author_name):
        with UseDatabase(config_dict) as cursor:
            sql = '''SELECT *
                            FROM book
                            WHERE book LIKE %s OR author LIKE %s'''
            cursor.execute(sql, (book_author_name, book_author_name,))
            books = cursor.fetchall()
            if not books:
                return []
        return books
