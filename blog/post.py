from errors import InputError
from render import render


class Post:
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
        with open('templates/base.html', 'r') as file:
            data = {'content': str(template_for_inheritance)}
            template = file.read()
            return render(template, data).encode('UTF-8')
