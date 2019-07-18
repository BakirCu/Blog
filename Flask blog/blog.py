from flask import Flask, render_template, request
from storage import Storage
from post import Post
app = Flask(__name__)


@app.route('/')
def home():
    all_posts = Storage.select_posts()
    return render_template('home.html',
                           posts=all_posts)


@app.route('/new_post')
def new_post():
    return render_template('new_post.html')


@app.route('/post_added', methods=['POST'])
def post_added():
    new_post = Post.read_post(request)
    Storage.add_post(new_post)
    return('succes')


@app.route('/view_post')
def view_post():

    post_id = request.args.get("post_id")

    post = Storage.select_post(post_id)

    return render_template('post_selected.html',
                           title=post[0],
                           post=post[3],
                           date=post[1])


app.run()
