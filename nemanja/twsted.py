from twisted.web import server, resource
from twisted.internet import reactor
from datetime import datetime
import random


class MojSajt(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        request.setHeader("Content-Type", "text/html")

        # localhost:8080/x?y=z&a=b
        # request.uri -> /x?y=z&a=b (od kose crte do kraja)
        # request.path -> /x (od kose crte do parametera)
        # request.args -> { 'y': 'z', 'a': 'b' } (svi parametri kao dict)

        # localhost:8080
        if request.uri == b"/":
            return "<html><h1>Hello, world!</h1></html>".encode('utf-8')
        # localhost:8080/bakir
        elif request.uri == b"/bakir":  # da li ovde moe da se koristi path?
            return "<html><h1>Hello, Bakir!</h1></html>".encode('utf-8')
        # localhost:8080/bakir
        elif request.uri == b"/time":
            return ("<html>" + str(datetime.now()) + "</html>").encode('utf-8')
        elif request.path == b"/random":
            from_num = 1
            to_num = 10

            # http://localhost:8080/random?from=100&to=200
            # print(request.uri) -> '/random?from=100&to=200'
            # print(request.path) -> '/random'
            # request.args -> { 'from': ['100'], 'to': ['200']}

            if b'from' in request.args:
                from_str = request.args[b'from']
                from_num = int(from_str[0])

            if b'to' in request.args:
                to_str = request.args[b'to']
                to_num = int(to_str[0])

            return ("<html>" + str(random.randint(from_num, to_num)) + "</html>").encode('utf-8')
        else:
            return "<html><h1>Hello, unknown person!</h1></html>".encode('utf-8')


site = server.Site(MojSajt())
reactor.listenTCP(8080, site)
reactor.run()
