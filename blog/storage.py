import mysql.connector
from configuration import Configuration
from data_base import UseDatabase
from errors import InputError


class Storage:

    config_dict = Configuration.get_config()

    def __init__(self, title, post):
        if not title or not post:
            raise InputError('Title and post must have some value')
        self.title = title
        self.post = post

    def read_post(request):
        title = request.args[b"title"][0].decode('UTF-8')
        post = request.args[b"post"][0].decode('UTF-8')
        return Storage(title, post)

    @staticmethod
    def add_post(new_post):
        conn = mysql.connector.connect(**Storage.config_dict)
        conn.autocommit = False
        cursor = conn.cursor()
        try:
            _SQL = '''INSERT INTO blog.posts(title, post)
                    VALUES (%s, %s);'''
            cursor.execute(_SQL, (new_post.title, new_post.post))

        except mysql.connector.errors.Error:
            return False

        cursor.close()
        conn.close()
        return True

    @staticmethod
    def select_all():
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''SELECT * FROM blog.posts
                         ORDER by time_post DESC;'''
            cursor.execute(_SQL)
            users = cursor.fetchall()
            if not users:
                return ''
            return users

    @staticmethod
    def select_post(title):
        with UseDatabase(Storage.config_dict) as cursor:
            _SQL = '''SELECT * FROM blog.posts
                         WHERE title LIKE %s '''
            cursor.execute(_SQL, (title,))
            users = cursor.fetchall()
            print(users)
            if not users:
                return ''
            return users[0]
