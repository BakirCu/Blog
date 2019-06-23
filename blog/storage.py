import mysql.connector
from configuration import Configuration
from data_base import UseDatabase
from errors import MySQLError


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
                raise MySQLError(str(err))

    @staticmethod
    def select_all():
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''SELECT * FROM blog.posts
                         ORDER by time_post DESC;'''
            cursor.execute(_SQL)
            users = cursor.fetchall()
            print(users)
            return users

    @staticmethod
    def select_post(title, post_content):
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''SELECT * FROM blog.posts
                         WHERE title LIKE %s and post LIKE %s'''
            cursor.execute(_SQL, (title, post_content))
            users = cursor.fetchall()
            print(users)
            return users[0]
