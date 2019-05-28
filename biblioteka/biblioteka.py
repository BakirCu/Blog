import time
from user import User
from book import Book
from user_book import UserBook
from errors import InputError
from configuration import Configuration


config_dict = Configuration.get_config()


def create_new_user():
    try:
        user = User.read_user()
        User.add_user(user)
    except InputError as err:
        print(err)


def create_new_book():
    try:
        book = Book.read_book()
        Book.add_book(book)
    except InputError as err:
        print(err)
    except ValueError as err:
        print(err, 'BOOK NUMBER must be int')


def search_print_user():
    search_user_str = input(
        'Input first name and last name for search:\n')
    try:
        user_file = User.search_user_name(search_user_str)
    except ValueError as err:
        print(err)
    else:
        items = User.search_user_database(user_file)
        if not items:
            print('No such file, try again \n')
        for item in items:
            print(item)


def search_print_book():
    search_book_str = input(
        'Input author name or book name for search:\n')
    try:
        book_file = Book.search_book_name(search_book_str)
    except InputError as err:
        print(err)
    else:
        items = Book.search_book_database(book_file)
        if not items:
            print('No such file, try again \n')
        for item in items:
            print(item)

# ova funkcija proverava koliko je korisnik uzeo knjiga


def books_rent_limit(list_of_rented_books):
    num_of_rented_books = str(list_of_rented_books)[2]
    if int(num_of_rented_books) > 3:
        raise InputError("You can't rent more than 3 books")


def rent_book():
    try:
        user_book_id = UserBook.read_user_book()
        list_of_rented_books = UserBook.rent_book(user_book_id)
        books_rent_limit(list_of_rented_books)
        print('DONE, you rent a book')
    except ValueError as err:
        print(err, 'user id, and book id, must be integer')
    except InputError as err:
        print(err)


def days_keeping_book(items):
    curent_time = time.gmtime()
    curent_date = int(time.strftime("%d", curent_time))
    rent_date = int(items[10:12])
    return curent_date - rent_date

# ovde korisnik ne moze da vrati pogresnu kljigu
# jer uporedjujem id kljige u bazi i one koju korisnik pokusava da vrati


def id_compare_rent_return_book(user_book_id, book_rent_id):
    if list(book_rent_id[0]) != [user_book_id.book_id]:
        raise InputError("You did't take that book")


def return_book():
    try:
        user_book_id = UserBook.read_user_book()
        book_rent_id = UserBook.id_return_book(user_book_id)
        id_compare_rent_return_book(user_book_id, book_rent_id)
        items = UserBook.date_return_book(user_book_id)
        items_str = str(items[0])
        having_book = days_keeping_book(items_str)
        print('You took book:', items_str[2:20])
        print('You have a book:', having_book, 'days')
    except ValueError as err:
        print(err, 'user id, and book id, must be integer')
    except InputError as err:
        print(err)
    except IndexError as err:
        print("You didn't rent a book, try again ", err)


def load_new_file():
    path = input('Input path of file \n')
    try:
        book_load_list = Book.load_book_file_to_list(path)
    except FileNotFoundError:
        print('No such file, try again')
    else:
        for line in book_load_list:
            Book.add_book(line)


def main():
    while True:
        choice = input(
            '\nChoice one of options: \n 1-input user'
            '\n 2-input book \n 3-search_user '
            ' \n 4-search_book \n 5-load_file \n 6-rent_book \n'
            ' 7-return_book \n 8-Exit \n')
        if choice == '8':
            break
        choices_dict = {'1': create_new_user,
                        '2': create_new_book,
                        '3': search_print_user,
                        '4': search_print_book,
                        '5': load_new_file,
                        '6': rent_book,
                        '7': return_book}
        if choice not in choices_dict:
            print('ENTER ONE OF NUMBERS')
        else:
            choices_dict[choice]()


main()
