from time import time
from configuration import Configuration
from data_base import UseDatabase

config_dict = Configuration.get_config()


def insert():
    with UseDatabase(config_dict) as cursor:
        sql = ''' INSERT INTO biblioteka.citanje value('123')'''
        cursor.execute(sql)


def main():
    for i in range(1000):
        insert()


start_time = time()
main()
end_time = time()
diferenc = end_time-start_time
print(diferenc)
print(10000/diferenc)
