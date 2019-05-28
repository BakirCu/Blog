from twisted.web import server, resource
from twisted.internet import reactor
from user import User
from book import Book
from errors import InputError


class MojSajt(resource.Resource):

    isLeaf = True

    def render_GET(self, request):
        request.setHeader("Content-Type", "text/html")

        if request.path == b"/":
            with open('templates\\index.html', 'r') as file:
                data = file.read()
                return data.encode('utf-8')

        elif request.path == b"/add_user":
            with open('templates\\add_user.html', 'r') as file:
                data = file.read()
                return data.encode('utf-8')

        elif request.path == b"/get_user":
            with open('templates\\get_user.html', 'r') as file:
                data = file.read()
                return data.encode('utf-8')

        elif request.path == b"/add_book":
            with open('templates\\add_book.html', 'r') as file:
                data = file.read()
                return data.encode('utf-8')

        elif request.path == b"/get_book":
            with open('templates\\get_book.html', 'r') as file:
                data = file.read()
                return data.encode('utf-8')

        elif request.path == b"/user_added":
            first_name = request.args[b"first_name"][0].decode('UTF-8')
            last_name = request.args[b"last_name"][0].decode('UTF-8')
            user_address = request.args[b"user_address"][0].decode('UTF-8')
            phone_numb = request.args[b"phone_numb"][0].decode('UTF-8')
            try:
                user = User(first_name, last_name, user_address, phone_numb)
                User.add_user(user)
            except InputError as err:
                return str(err).encode('UTF-8')
            if user:
                return "User {} {} successfuly added!".format(first_name, last_name).encode('utf-8')
            else:
                return "User {} don't exist!, Try again!".format(first_name)

        elif request.path == b"/user_geted":
            user_file = request.args[b"first_last_name"][0].decode('UTF-8')
            try:
                user_file = User.search_user_name(user_file)
            except ValueError as err:
                return str(err).encode('UTF-8')
            else:
                items = User.search_user_database(user_file)
                if not items:
                    return 'No such file, try again'.encode('UTF-8')
                for item in items:
                    return 'User {}, {} with id:{}  from {} is in database'.format(item[1], item[2], item[0], item[3]).encode('utf-8')

        elif request.path == b"/book_added":
            book_name = request.args[b"book_name"][0].decode('UTF-8')
            author_name = request.args[b"author_name"][0].decode('UTF-8')
            book_num = request.args[b"book_num"][0].decode('UTF-8')
            try:
                book = Book(book_name, author_name, book_num)
                Book.add_book(book)
            except InputError as err:
                return str(err).encode('utf-8')
            except ValueError as err:
                full_err = str(err) + ' BOOK NUMBER must be int'
                return full_err.encode('UTF-8')
            if book:
                return '{} books {} written by {} successfuly added'.format(book_num, book_name, author_name).encode('utf-8')
            else:
                return "Book {} did't added! Try again!".format(book_name)

        elif request.path == b"/book_geted":
            book_file = request.args[b"book_author_name"][0].decode('UTF-8')
            try:
                book_file = Book.search_book_name(book_file)
            except InputError as err:
                return str(err).encode('utf-8')
            else:
                items = Book.search_book_database(book_file)
                if not items:
                    return 'No such file, try again'.encode('utf-8')
                for item in items:
                    return 'Book {}, written by {} is in database'.format(item[0], item[1]).encode('utf-8')

        return "Nepoznata putanja".encode('utf-8')


site = server.Site(MojSajt())
reactor.listenTCP(8080, site)
reactor.run()
