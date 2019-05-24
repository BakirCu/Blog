import mysql.connector


class Configuration:
    config_dict = {'user': 'root', 'password': 'password',
                   'host': 'localhost',
                   'database': 'biblioteka1'}

    @staticmethod
    def get_config():
        return Configuration.config_dict


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
