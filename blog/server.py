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
        try:
            page = request.args[b"page"][0].decode('UTF-8')
            page_size = request.args[b"page_size"][0].decode('UTF-8')
        except Exception:
            template, data = InputError.raise_error(
                "Check:'page' and 'page_size'")
            template_content = render(template, data)
            return Post.read_base_template(template_content)

        if not page.isnumeric() or not page_size.isnumeric():
            template, data = InputError.raise_error(
                'Page and page_size must be positive numbers')
            template_content = render(template, data)
            return Post.read_base_template(template_content)

        return MojSajt.get_posts_from_to(request, int(page), int(page_size))

    @staticmethod
    def get_posts_from_to(request, page, page_size):
        if page < 1 or page_size < 1:
            template, data = InputError.raise_error(
                'Page must be positive nuber')
            template_content = render(template, data)
            return Post.read_base_template(template_content)

        page_previous_num = page - 1

        link_next_template = '<a href="/get_posts?page={}&page_size={}"> Next </a>'
        link_next = link_next_template.format(str(page + 1), str(page_size))

        link_prev_template = '<a href="/get_posts?page={}&page_size={}"> Previous </a>'
        link_previous = link_prev_template.format(
            str(page_previous_num), str(page_size))

        post_len = Storage.post_len()

        if page * page_size >= post_len:
            link_next = ''

        if page == 1:
            link_previous = ''

        all_posts = Storage.select_posts(
            (page-1)*page_size, page_size)

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

        data_small = {'posts': all_posts_list,
                      'next': link_next,
                      'previous': link_previous}

        with open('templates/home.html', 'r') as file:
            template_small = file.read()
            template_content = render(template_small, data_small)

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
                              b"/post_added": MojSajt.render_POST,
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

    def render_POST(self, request):
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


site = server.Site(MojSajt())
reactor.listenTCP(8080, site)
reactor.run()
