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
    def select_posts(page, page_size):
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''SELECT * FROM blog.posts
                         ORDER by time_post DESC
                         LIMIT %s,%s;'''
            cursor.execute(_SQL, (page, page_size))
            posts = cursor.fetchall()

            return posts

    @staticmethod
    def select_post(post_id):
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''SELECT * FROM blog.posts
                         WHERE post_id = %s'''
            cursor.execute(_SQL, (post_id,))
            post = cursor.fetchall()
            return post[0]

    @staticmethod
    def post_len():
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''select count(*) FROM blog.posts'''
            cursor.execute(_SQL)
            post_len = cursor.fetchall()
            return post_len[0][0]

    @staticmethod
    def add_user(new_user):
        with UseDatabase(Storage.config_dict) as cursor:
            try:
                _SQL = '''INSERT INTO blog.users(username, password)
                        VALUES (%s, %s);'''
                cursor.execute(_SQL, (new_user.username, new_user.password))
            except mysql.connector.errors.IntegrityError:
                raise MySQLError(
                    'This  username is taken. Please chouse another username!')
            except mysql.connector.errors.Error as err:
                raise MySQLError(str(err))

    @staticmethod
    def select_user(username, password):
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''SELECT * FROM blog.users
                            WHERE username = %s and password = %s'''
            cursor.execute(_SQL, (username, password))
            user = cursor.fetchall()
            return user
