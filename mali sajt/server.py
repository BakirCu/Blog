from twisted.web import server, resource
from twisted.internet import reactor
from storage import Storage


class MojSajt(resource.Resource):
    isLeaf = True

    def __init__(self):
        self.values = Storage()

    def render_GET(self, request):
        request.setHeader("Content-Type", "text/html")

        if request.path == b"/":
            with open('index.html', 'r') as file:
                data = file.read()
                return data.encode('utf-8')

        elif request.path == b"/add":
            with open('add.html', 'r') as file:
                data = file.read()
                return data.encode('utf-8')

        elif request.path == b"/get":
            with open('get.html', 'r') as file:
                data = file.read()
                return data.encode('utf-8')

        elif request.path == b"/neka_putanja":
            key = request.args[b"bakir_kljuc"][0].decode('UTF-8')
            value = request.args[b"bakir_vrednost"][0].decode('UTF-8')
            key_value = self.values.add(key, value)
            if key_value:
                return "Uspesno ste dodali kljuc {} sa vrednoscu {}!".format(key, value).encode('utf-8')
            else:
                return 'Kljuc {} vec postoji!'.format(key)

        elif request.path == b"/vrati_vrednost":
            key = request.args[b"moj_kljuc"][0].decode('UTF-8')
            value = self.values.select(key)
            if value:
                return "Vrednost za kljuc {} je: {}".format(key, value).encode('utf-8')
            else:
                return "Kljuc {} ne postoji".format(key).encode('utf-8')
        return "Nepoznata putanja".encode('utf-8')


site = server.Site(MojSajt())
reactor.listenTCP(8080, site)
reactor.run()
