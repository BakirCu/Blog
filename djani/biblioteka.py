import mysql.connector
import time

config_dict = {'user': 'root', 'password': 'password',
               'host': 'localhost',
               'database': 'biblioteka1'}


class UseDatabase:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


class InputError(Exception):
    pass


class User:
    def __init__(self, first_name, last_name, user_address, phone_numb):
        if not first_name or not last_name \
                or not user_address or not phone_numb:
            raise InputError("Every positional argument: 'first_name'"
                             "'last_name', 'user_address', 'phone_num', "
                             "must have some value")
        self.first_name = first_name
        self.last_name = last_name
        self.user_address = user_address
        self.phone_numb = phone_numb

    @staticmethod
    def read_user():
        first_name = input('Input first name of user').strip()
        last_name = input('Input last name of user').strip()
        user_address = input('Input user address').strip()
        phone_numb = input('Input user phone number').strip()
        return User(first_name, last_name, user_address, phone_numb)

    @staticmethod
    def add_user(user):
        with UseDatabase(config_dict) as cursor:
            _SQL = '''INSERT INTO user ( first_name, last_name,
                                user_address, phone_numb)\
                                     VALUES( %s, %s, %s, %s)'''
            cursor.execute(_SQL, (user.first_name, user.last_name,
                                  user.user_address, user.phone_numb))

    @staticmethod
    def search_user_name(name_str):
        name_list = name_str.strip().split()
        if not name_list or len(name_list) != 2:
            raise ValueError("Must enter fist and last name, space separated")
        return name_list

    @staticmethod
    def search_user_database(first_last_name):
        first_name = first_last_name[0].strip()
        last_name = first_last_name[1].strip()
        with UseDatabase(config_dict) as cursor:
            sql = '''SELECT *
                        FROM user
                        WHERE first_name LIKE %s and last_name LIKE %s'''
            cursor.execute(sql, (first_name, last_name,))
            users = cursor.fetchall()
            if not users:
                return []
        return users


class Book:
    def __init__(self, book, author, book_num):
        if not book or not author or not book_num:
            raise InputError(
                "Every positional argument: 'book', 'author', \
                    'book_num', must have some value")
        self.book = book
        self.author = author
        self.book_num = abs(book_num)

    @staticmethod
    def read_book():
        book = input('Input book name')
        author = input('Input author of book')
        book_num = int(input('Input numbers of book'))
        return Book(book, author, book_num)

    @staticmethod
    def add_book(user):
        with UseDatabase(config_dict) as cursor:
            sql = '''INSERT INTO book(book, author, book_num)
                        VALUES(%s, %s, %s)
                        ON DUPLICATE KEY UPDATE \
                            book_num = VALUES(book_num) + book_num'''
            cursor.execute(sql, (user.book, user.author, user.book_num))

    @staticmethod
    def search_book_name(name_str):
        name = name_str.strip()
        if not name:
            raise InputError('Input must have some value')
        return name

    @staticmethod
    def search_book_database(first_last_name):
        name = first_last_name
        with UseDatabase(config_dict) as cursor:
            sql = '''SELECT *
                            FROM book
                            WHERE book LIKE %s OR author LIKE %s'''
            cursor.execute(sql, (name, name,))
            users = cursor.fetchall()
            if not users:
                return []
        return users

    @staticmethod
    def load_book_file_to_list(path):

        with open(path) as input_file:
            whole_file = input_file.read()
            lines = whole_file.splitlines()
            lines_list = [list(map(str.strip, item.split(',')))
                          for item in lines]

        return lines_list


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

            # Sta sve moze da podje naopako:
            # 1) Mozes da uneses NULL za user_id ili book_id -> IntegrityError
            # 2) Mozes umesto brojeva da uneses pogresan tip DatabaseError
            # 3) Moze da se unese user_id nepostojeceg usera -> IntegrityError
            # 4) Isto to, samo za knjige -> IntegrityError
            # 5) Moze dvaput isti korisnik da unese -> IntegrityError

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
            # OVO PROVERI ZASTO NE RADI ALTER TABLE CHECK(rent_num <= 3)
            sql5 = '''UPDATE biblioteka1.user
                    SET rent_num = rent_num + 1
                    WHERE user_id = %(user_id)s'''
            cursor.execute(sql5, {'user_id': user_book.user_id})

            # Sta ovde moze da podje naopako:
            # 1) Moze book_id da bude NULL -> IntegrityError
            # 2) Moze da bude pogresan tip book_id -> DatabaseError
            # 3) Moze da ne postoji knjiga za taj id -> IntegrityError
            # 4) Moze da book_num bude 0 pre izvrsavanja -> DatabaseError

            sql1 = '''UPDATE book
                    SET book_num = book_num - 1
                    WHERE book_id = %(book_id)s'''
            cursor.execute(sql1, {'book_id': user_book.book_id})

            conn.commit()
            return numbers_book_id
        except mysql.connector.errors.IntegrityError as err:
            print('IntegrityError: ', err)
            conn.rollback()
        except mysql.connector.errors.DatabaseError as err:
            print('DatabaseError: ', err)
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
        return book_id_from_user_book


def create_new_user():
    try:
        user = User.read_user()
        User.add_user(user)
    except InputError as err:
        print(err)


def create_new_book():
    try:
        book = Book.read_book()
        Book.add_book(book)
    except InputError as err:
        print(err)
    except ValueError as err:
        print(err, 'BOOK NUMBER must be int')


def search_print_user():
    search_user_str = input(
        'Input first name and last name for search:\n')
    try:
        user_file = User.search_user_name(search_user_str)
    except ValueError as err:
        print(err)
    else:
        items = User.search_user_database(user_file)
        if not items:
            print('No such file, try again \n')
        for item in items:
            print(item)


def search_print_book():
    search_book_str = input(
        'Input author name or book name for search:\n')
    try:
        book_file = Book.search_book_name(search_book_str)
    except InputError as err:
        print(err)
    else:
        items = Book.search_book_database(book_file)
        if not items:
            print('No such file, try again \n')
        for item in items:
            print(item)

# ova funkcija proverava koliko je korisnik uzeo knjiga


def books_rent_limit(list_of_rented_books):
    num_of_rented_books = str(list_of_rented_books)[2]
    if int(num_of_rented_books) > 3:
        raise InputError("You can't rent more than 3 books")


def rent_book():
    try:
        user_book_id = UserBook.read_user_book()
        list_of_rented_books = UserBook.rent_book(user_book_id)
        books_rent_limit(list_of_rented_books)
        print('DONE, you rent a book')
    except ValueError as err:
        print(err, 'user id, and book id, must be integer')
    except InputError as err:
        print(err)


def days_keeping_book(items):
    curent_time = time.gmtime()
    curent_date = int(time.strftime("%d", curent_time))
    rent_date = int(items[10:12])
    return curent_date - rent_date

# ovde korisnik ne moze da vrati pogresnu kljigu
# jer uporedjujem id kljige u bazi i one koju korisnik pokusava da vrati


def id_compare_rent_return_book(user_book_id, book_rent_id):
    if list(book_rent_id[0]) != [user_book_id.book_id]:
        raise InputError("You did't take that book")


def return_book():
    try:
        user_book_id = UserBook.read_user_book()
        book_rent_id = UserBook.id_return_book(user_book_id)
        id_compare_rent_return_book(user_book_id, book_rent_id)
        items = UserBook.date_return_book(user_book_id)
        items_str = str(items[0])
        having_book = days_keeping_book(items_str)
        print('You took book:', items_str[2:20])
        print('You have a book:', having_book, 'days')
    except ValueError as err:
        print(err, 'user id, and book id, must be integer')
    except InputError as err:
        print(err)
    except IndexError as err:
        print("You didn't rent a book, try again ", err)


def load_new_file():
    path = input('Input path of file \n')
    try:
        book_load_list = Book.load_book_file_to_list(path)
    except FileNotFoundError:
        print('No such file, try again')
    else:
        for line in book_load_list:
            Book.add_book(line)


def main():
    while True:
        choice = input(
            '\nChoice one of options: \n 1-input user'
            '\n 2-input book \n 3-search_user '
            ' \n 4-search_book \n 5-load_file \n 6-rent_book \n'
            ' 7-return_book \n 8-Exit \n')
        if choice == '8':
            break
        choices_dict = {'1': create_new_user,
                        '2': create_new_book,
                        '3': search_print_user,
                        '4': search_print_book,
                        '5': load_new_file,
                        '6': rent_book,
                        '7': return_book}
        if choice not in choices_dict:
            print('ENTER ONE OF NUMBERS')
        else:
            choices_dict[choice]()


main()
