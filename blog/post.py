from errors import InputError
from render import render


class Post:
    with open('templates/base.html', 'r') as file:
        template = file.read()

    def __init__(self, title, post):
        if not title or not post:
            raise InputError('Title and post must have some value')
        self.title = title
        self.post = post

    @staticmethod
    def read_post(request):
        title = request.args[b"title"][0].decode('UTF-8')
        post = request.args[b"post"][0].decode('UTF-8')
        return Post(title, post)

    @staticmethod
    def read_base_template(template_for_inheritance):
        data = {'content': str(template_for_inheritance)}
        return render(Post.template, data).encode('UTF-8')
