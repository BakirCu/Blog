from twisted.web import server, resource
from twisted.internet import reactor
from storage import Storage
from errors import InputError, MySQLError
from render import render
from post import Post


class MojSajt(resource.Resource):
    isLeaf = True

    def render_GET(self, request):

        route_choice_dict = {
            b"/new_post": ('templates/new_post.html', "text/html"),
        }

        if request.path in route_choice_dict:
            try:
                request.setHeader(
                    "Content-Type", route_choice_dict[request.path][1])
                with open(route_choice_dict[request.path][0], 'r') as file:
                    template_content = file.read()
                return Post.read_base_template(template_content)
            except MySQLError as err:
                template, data = InputError.raise_error(str(err))
                template_content = render(template, data)
                return Post.read_base_template(template_content)

        elif request.path == b"/":
            request.setHeader("Content-Type", "text/html")
            with open('templates/home.html', 'r') as file:
                template_smal = file.read()
                all_posts = Storage.select_posts(0, 7)
                all_posts_list = []

                for post in all_posts:

                    post_dict = {'title': post[0],
                                 'post': post[3],
                                 'date': str(post[1]),
                                 'id': str(post[2])
                                 }
                    all_posts_list.append(post_dict)
                data_smal = {'posts': all_posts_list}
                post_len = Storage.post_len()

                if post_len > 7:
                    data_smal['next'] = '<a href="/get_posts?page=2&page_size=7"> Next </a>'

                else:
                    data_smal['next'] = ''
                template_content = render(template_smal, data_smal)

                return Post.read_base_template(template_content)

        elif request.path == b"/get_posts":
            print(request.uri)
            page = request.args[b"page"][0].decode('UTF-8')
            page_size = request.args[b"page_size"][0].decode('UTF-8')
            page_num = int(page)
            page_size_num = int(page_size)
            page_next_num = page_num + 1
            page_next_str = str(page_next_num)
            aderss = '<a href="/get_posts?page={}&page_size={}"> Next </a>'.format(
                page_next_str, str(page_size_num))
            return aderss.encode('utf-8')

        elif request.path == b"/post_added":
            try:
                new_post = Post.read_post(request)
                Storage.add_post(new_post)
                data_smal = {'title': new_post.title,
                             'post': new_post.post}
                with open('templates/tamplate_result/post_added.html', 'r') as file:
                    template_smal = file.read()
                    template_content = render(template_smal, data_smal)
                    return Post.read_base_template(template_content)

            except InputError as err:
                template, data = InputError.raise_error(str(err))
                template_content = render(template, data)
                return Post.read_base_template(template_content)
            except Exception as err:
                template, data = InputError.raise_error(str(err))
                template_content = render(template, data)
                return Post.read_base_template(template_content)

        elif request.path == b"/view_post":
            request.setHeader("Content-Type", "text/html")
            with open('templates/view_post.html', 'r') as file:
                template_content = file.read()
                try:
                    title = request.args[b"post_name"][0].decode('UTF-8')
                    post_id = request.args[b"post_id"][0].decode(
                        'UTF-8')
                    post = Storage.select_post(title, post_id)
                    print(post)
                    data = {'title': post[0],
                            'post': post[3],
                            'date': str(post[1]),
                            'id': str(post[2])}
                    with open('templates/tamplate_result/post_selected.html', 'r') as file:
                        template = file.read()
                    template_content = render(template, data)
                    return Post.read_base_template(template_content)
                except Exception as err:
                    template, data = InputError.raise_error(str(err))
                    template_content = render(template, data)
                    return Post.read_base_template(template_content)

        template, data = InputError.raise_error('Unknown rout')
        template_content = render(template, data)
        return Post.read_base_template(template_content)


site = server.Site(MojSajt())
reactor.listenTCP(8080, site)
reactor.run()
