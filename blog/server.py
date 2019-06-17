from twisted.web import server, resource
from twisted.internet import reactor
from storage import Storage
from errors import InputError
from render import render
from post import Post


class MojSajt(resource.Resource):
    isLeaf = True

    def render_GET(self, request):

        route_choice_dict = {
            b"/new_post": ('templates/new_post.html', "text/html"),
        }

        if request.path in route_choice_dict:
            request.setHeader(
                "Content-Type", route_choice_dict[request.path][1])
            with open(route_choice_dict[request.path][0], 'r') as file:
                data = file.read()
                return data.encode('utf-8')

        elif request.path == b"/":
            request.setHeader("Content-Type", "text/html")
            with open('templates/home.html', 'r') as file:
                template = file.read()
                all_posts = Storage.select_all()
                all_posts_list = []
                for post in all_posts:
                    post_dict = {'title': post[1],
                                 'post': post[0],
                                 'date': str(post[2])
                                 }
                    all_posts_list.append(post_dict)
                data = {'posts': all_posts_list}
                return render(template, data).encode('utf-8')

        elif request.path == b"/post_added":
            try:
                new_post = Post.read_post(request)
                post = Storage.add_post(new_post)
                if not post:
                    template, data = InputError.raise_error(
                        'Inpit another title: this title alredy exist')
                    return render(template, data).encode('UTF-8')
            except InputError as err:
                template, data = InputError.raise_error(str(err))
                return render(template, data).encode('UTF-8')
            except Exception as err:
                template, data = InputError.raise_error(str(err))
                return render(template, data).encode('UTF-8')

            if new_post:
                data = {'title': new_post.title,
                        'post': new_post.post}
                with open('templates/tamplate_result/post_added.html', 'r') as file:
                    template = file.read()
                return render(template, data).encode('utf-8')

        elif request.path == b"/view_post":
            request.setHeader("Content-Type", "text/html")
            with open('templates/view_post.html', 'r') as file:
                template = file.read().encode('utf-8')
                try:
                    title = request.args[b"post_name"][0].decode('UTF-8')
                    post = Storage.select_post(title)
                except Exception as err:
                    template, data = InputError.raise_error(str(err))
                    return render(template, data).encode('UTF-8')

                if post:
                    data = {'title': post[1],
                            'post': post[0],
                            'date': str(post[2])}
                    with open('templates/tamplate_result/post_selected.html', 'r') as file:
                        template = file.read()
                    return render(template, data).encode('utf-8')

        template, data = InputError.raise_error('Unknown rout')
        return render(template, data).encode('UTF-8')


site = server.Site(MojSajt())
reactor.listenTCP(8080, site)
reactor.run()
