from errors import InputError


class Post:
    def __init__(self, title, post):
        if not title or not post:
            raise InputError('Title and post must have some value')
        self.title = title
        self.post = post

    def read_post(request):
        title = request.args[b"title"][0].decode('UTF-8')
        post = request.args[b"post"][0].decode('UTF-8')
        return Post(title, post)
