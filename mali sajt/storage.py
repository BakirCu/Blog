import mysql.connector
from configuration import Configuration, UseDatabase


class Storage():
    def __init__(self):

        self.config_dict = Configuration.get_config()

    def add(self, key, value):
        with UseDatabase(self.config_dict) as cursor:
            try:
                _SQL = '''INSERT INTO biblioteka.kljuc_vrednost(Kljuc, Vrednost)
                        VALUES (%s, %s);'''
                cursor.execute(_SQL, (key, value))

            except mysql.connector.errors.IntegrityError:
                return False
            return True

    def select(self, key):
        with UseDatabase(self.config_dict) as cursor:
            _SQL = '''SELECT Kljuc, Vrednost
                            FROM biblioteka.kljuc_vrednost
                            WHERE Kljuc = %(key)s'''
            cursor.execute(_SQL, {'key': key})
            users = cursor.fetchall()
            if not users:
                return ''
            return users[0][1]
