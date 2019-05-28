import mysql.connector
from configuration import Configuration
from data_base import UseDatabase

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
