import mysql.connector
from configuration import Configuration
from data_base import UseDatabase
from errors import InputError
import time

config_dict = Configuration.get_config()


class UserBook:
    def __init__(self, user_id, book_id):

        self.user_id = user_id
        self.book_id = book_id

    @staticmethod
    def read_user_book():
        user_id = int(input('input user id').strip())
        book_id = int(input('input book id').strip())
        return UserBook(user_id, book_id)

    @staticmethod
    def rent_book(user_book):
        conn = mysql.connector.connect(**config_dict)
        conn.autocommit = False
        cursor = conn.cursor()

        try:

            sql = '''INSERT INTO user_book(user_id, book_id)
                            VALUES(%s, %s)'''
            cursor.execute(sql, (user_book.user_id, user_book.book_id))

            sql3 = '''INSERT INTO history_book(user_id, book_id)
                            VALUES(%s, %s)'''
            cursor.execute(sql3, (user_book.user_id, user_book.book_id))

            sql2 = '''SELECT count(user_id) FROM biblioteka1.user_book
                    WHERE user_id = %(user_id)s
                    GROUP BY user_id'''
            cursor.execute(sql2, {'user_id': user_book.user_id})
            numbers_book_id = cursor.fetchall()

            sql5 = '''UPDATE biblioteka1.user
                    SET rent_num = rent_num + 1
                    WHERE user_id = %(user_id)s'''
            cursor.execute(sql5, {'user_id': user_book.user_id})

            sql1 = '''UPDATE book
                    SET book_num = book_num - 1
                    WHERE book_id = %(book_id)s'''
            cursor.execute(sql1, {'book_id': user_book.book_id})

            conn.commit()
            return numbers_book_id
        except mysql.connector.errors.IntegrityError as err:
            full_err = 'IntegrityError: ' + str(err)
            return full_err.encode('utf-8')
            conn.rollback()
        except mysql.connector.errors.DatabaseError as err:
            full_err = 'DataBaseError: ' + str(err)
            return full_err.encode('utf-8')
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def date_return_book(user_book):
        conn = mysql.connector.connect(**config_dict)
        conn.autocommit = False
        cursor = conn.cursor()

        try:

            sql3 = '''SELECT @rent:=date FROM biblioteka1.user_book
                                WHERE user_id = %(user_id)s '''
            cursor.execute(sql3, {'user_id': user_book.user_id})
            rent_date = cursor.fetchall()

            sql1 = '''DELETE from biblioteka1.user_book
                WHERE user_id = %(user_id)s and book_id = %(book_id)s'''

            cursor.execute(sql1, {'user_id': user_book.user_id,
                                  'book_id': user_book.book_id})

            sql2 = '''UPDATE biblioteka1.book
                    SET book_num = book_num + 1
                    WHERE book_id = %(book_id)s'''
            cursor.execute(sql2, {'book_id': user_book.book_id})
            sql4 = '''UPDATE biblioteka1.history_book
                    SET return_date = CURRENT_TIMESTAMP
                    WHERE user_id = %(user_id)s'''
            cursor.execute(sql4, {'user_id': user_book.user_id})
            conn.commit()
            return rent_date

        except mysql.connector.errors.Error as err:
            print(err)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def id_return_book(user_book):
        with UseDatabase(config_dict) as cursor:
            sql = '''SELECT book_id FROM biblioteka1.user_book
            WHERE user_id = %(user_id)s'''
            cursor.execute(sql, {'user_id': user_book.user_id})
            book_id_from_user_book = cursor.fetchall()
        return [item[0] for item in book_id_from_user_book]

    @staticmethod
    def books_rent_limit(list_of_rented_books):
        num_of_rented_books = str(list_of_rented_books)[2]
        if int(num_of_rented_books) > 3:
            raise InputError("You can't rent more than 3 books")

    @staticmethod
    def days_keeping_book(items):
        curent_time = time.gmtime()
        curent_date = int(time.strftime("%d", curent_time))
        rent_date = int(items[10:12])
        return curent_date - rent_date


def id_compare_rent_return_book(user_book_id, book_rent_id):
    if int(user_book_id.book_id) not in book_rent_id:
        raise InputError("You did't take that book")
