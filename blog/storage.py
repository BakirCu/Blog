import mysql.connector
from configuration import Configuration
from data_base import UseDatabase
from errors import InputError


class Storage:

    config_dict = Configuration.get_config()

    @staticmethod
    def add_post(new_post):
        with UseDatabase(Storage.config_dict) as cursor:
            try:
                _SQL = '''INSERT INTO blog.posts(title, post)
                        VALUES (%s, %s);'''
                cursor.execute(_SQL, (new_post.title, new_post.post))
            except mysql.connector.errors.Error as err:
                raise InputError(str(err))

    @staticmethod
    def select_all():
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''SELECT * FROM blog.posts
                         ORDER by time_post DESC;'''
            cursor.execute(_SQL)
            users = cursor.fetchall()
            return users

    @staticmethod
    def select_post(title):
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''SELECT * FROM blog.posts
                         WHERE title LIKE %s '''
            cursor.execute(_SQL, (title,))
            users = cursor.fetchall()
            return users[0]
