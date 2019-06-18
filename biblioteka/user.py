from errors import InputError
from configuration import Configuration
from data_base import UseDatabase


config_dict = Configuration.get_config()


class User:
    def __init__(self, first_name, last_name, user_address, phone_numb):
        if not first_name or not last_name \
                or not user_address or not phone_numb:

            raise InputError("Every positional argument: 'first_name'"
                             "'last_name', 'user_address', 'phone_num', "
                             "must have some value")
        if not phone_numb.isnumeric():
            raise InputError('Phone number must be integer')
        if not first_name.isalpha() or not last_name.isalpha():
            raise InputError('First and last name must be alpha ')
        self.first_name = first_name
        self.last_name = last_name
        self.user_address = user_address
        self.phone_numb = phone_numb

    @staticmethod
    def read_user(request):
        first_name = request.args[b"first_name"][0].decode('UTF-8')
        last_name = request.args[b"last_name"][0].decode('UTF-8')
        user_address = request.args[b"user_address"][0].decode('UTF-8')
        phone_numb = request.args[b"phone_numb"][0].decode('UTF-8')

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
        return list(users)
