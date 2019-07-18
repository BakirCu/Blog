from errors import InputError


class Post:
    def __init__(self, title, post):
        if not title or not post:
            raise InputError('Title and post must have some value')
        self.title = title
        self.post = post

    @staticmethod
    def read_post(request):
        title = request.form["title"]
        post = request.form["post"]
        return Post(title, post)
