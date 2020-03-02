class Configuration:
    config_dict = {'user': 'root', 'password': 'password',
                   'host': 'localhost',
                   'database': 'biblioteka1'}

    @staticmethod
    def get_config():
        return Configuration.config_dict
