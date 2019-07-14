from twisted.web import server, resource
from twisted.internet import reactor
from storage import Storage
from errors import InputError, MySQLError
from render import render
from post import Post


class MojSajt(resource.Resource):
    isLeaf = True

    @staticmethod
    def home(request):
        return MojSajt.get_posts_from_to(request, 1, 7)

    @staticmethod
    def get_posts(request):
        page = request.args[b"page"][0].decode('UTF-8')
        page_size = request.args[b"page_size"][0].decode('UTF-8')

        return MojSajt.get_posts_from_to(request, page, page_size)

    @staticmethod
    def get_posts_from_to(request, page, page_size):
        page_num = int(page)
        page_size_num = int(page_size)

        if page_num < 1:
            template, data = InputError.raise_error(
                'Page must be pozitive nuber')
            template_content = render(template, data)
            return Post.read_base_template(template_content)

        page_next_num = page_num + 1
        page_previous_num = page_num - 1
        page_previous_str = str(page_previous_num)
        page_next_str = str(page_next_num)
        link_next_page = '<a href="/get_posts?page={}&page_size={}"> Next </a>'.format(
            page_next_str, str(page_size_num))
        link_previous_page = '<a href="/get_posts?page={}&page_size={}"> Previous </a>'.format(
            page_previous_str, str(page_size_num))
        with open('templates/home.html', 'r') as file:
            template_smal = file.read()
            all_posts = Storage.select_posts(
                (page_num-1)*page_size_num, page_size_num)

            if len(all_posts) < page_previous_num:
                link_next_page = ''
            if not all_posts:
                template, data = InputError.raise_error(
                    'No more posts to show')
                template_content = render(template, data)
                return Post.read_base_template(template_content)

            all_posts_list = []
            for post in all_posts:

                post_dict = {'title': post[0],
                             'post': post[3],
                             'date': str(post[1]),
                             'id': str(post[2])
                             }
                all_posts_list.append(post_dict)
            data_smal = {'posts': all_posts_list,
                         'next': link_next_page,
                         'previous': link_previous_page}
        template_content = render(template_smal, data_smal)

        return Post.read_base_template(template_content)

    @staticmethod
    def post_added(request):
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

    @staticmethod
    def view_post(request):
        request.setHeader("Content-Type", "text/html")
        with open('templates/base.html', 'r') as file:
            template_content = file.read()
            try:

                post_id = request.args[b"post_id"][0].decode(
                    'UTF-8')
                post = Storage.select_post(post_id)

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

    def render_GET(self, request):
        dinamic_rouds_dict = {b"/": MojSajt.home,
                              b"/get_posts": MojSajt.get_posts,
                              b"/post_added": MojSajt.post_added,
                              b"/view_post": MojSajt.view_post}

        static_rouds_dict = {
            b"/new_post": ('templates/new_post.html', "text/html"),
        }

        if request.path in static_rouds_dict:
            try:
                request.setHeader(
                    "Content-Type", static_rouds_dict[request.path][1])
                with open(static_rouds_dict[request.path][0], 'r') as file:
                    template_content = file.read()
                return Post.read_base_template(template_content)
            except MySQLError as err:
                template, data = InputError.raise_error(str(err))
                template_content = render(template, data)
                return Post.read_base_template(template_content)

        elif request.path in dinamic_rouds_dict:
            return dinamic_rouds_dict[request.path](request)

        template, data = InputError.raise_error('Unknown rout')
        template_content = render(template, data)
        return Post.read_base_template(template_content)


site = server.Site(MojSajt())
reactor.listenTCP(8080, site)
reactor.run()
