from flask import Flask, render_template, request, Markup, session, redirect, url_for
from storage import Storage
from post import PostCreate, Post
from user import UserCreate
from errors import InputError, MySQLError
from functools import wraps
from base64 import b64encode

app = Flask(__name__)
app.secret_key = 'any random string'


def check_logged_in(func):
    @wraps(func)
    def omotac(*args, **kwargs):
        if 'log_in' in session:
            return func(*args, **kwargs)
        return render_template('check_logged_in.html', value='logged out', user="please log in")
    return omotac


def get_posts_from_to(page, page_size):

    li_home = Markup('<li class="nav-item" >')
    li_new_post = Markup('<li class="nav-item " >')

    if page < 1 or page_size < 1:
        return InputError.raise_error('Page must be positive nuber')
    link_next_template = Markup(
        '<a class="page-link" href="/get_posts?page={}&page_size={}"> Next </a>')
    link_next = link_next_template.format(str(page + 1), str(page_size))

    link_prev_template = Markup(
        '<a class="page-link" href="/get_posts?page={}&page_size={}"> Previous </a>')
    link_previous = link_prev_template.format(str(page - 1), str(page_size))

    post_len = Storage.post_len()
    if page * page_size >= post_len:
        link_next = ''
    if page == 1:
        link_previous = ''
        li_home = Markup('<li class="nav-item active" >')

    posts_from_to = Storage.select_posts(
        (page-1)*page_size, page_size)
    # ovde pravim listu objekata, da bi posle mogao lepo da prikazem u for petlji
    posts = []

    for post in posts_from_to:

        if not post[4]:
            image = ''
        else:
            image = b64encode(post[4]).decode("utf-8")

        posts.append(Post(post[0], post[1], post[2],
                          post[3], image))

    if not posts_from_to:
        return InputError.raise_error('No more posts to show')

    return render_template('home.html', li_home=li_home, li_new_post=li_new_post, posts=posts, next=link_next, previous=link_previous)


@app.route('/')
def home():
    return get_posts_from_to(1, 7)


@app.route('/new_post')
@check_logged_in
def new_post():

    li_home = Markup('<li class="nav-item ">')
    li_new_post = Markup('<li class="nav-item active" >')
    name = session['log_in']
    return render_template('new_post.html', li_home=li_home, li_new_post=li_new_post, name=name)


@app.route('/post_added', methods=['POST'])
def post_added():
    try:
        new_post = PostCreate.read_post(request)
        Storage.add_post(new_post)
        return render_template('post_added.html',
                               title=new_post.title,
                               post=new_post.post)
    except InputError as err:
        return InputError.raise_error(str(err))
    except Exception as err:
        return InputError.raise_error(str(err))


@app.route('/get_posts')
def get_posts():
    try:
        page = request.args.get("page")
        page_size = request.args.get("page_size")
    except Exception:
        return InputError.raise_error("Something get wrong whit:'page' or 'page_size'")
    if not page or not page_size:
        return InputError.raise_error("Check:'page' and 'page_size'")

    if not page.isnumeric() or not page_size.isnumeric():
        return InputError.raise_error('Page and page_size must be positive numbers')
    return get_posts_from_to(int(page), int(page_size))


@app.route('/view_post')
def view_post():
    try:
        post_id = request.args.get("post_id")
        post = Storage.select_post(post_id)
        return render_template('post_selected.html',
                               title=post[0],
                               post=post[3],
                               date=post[1])
    except Exception as err:
        return InputError.raise_error(str(err))


@app.errorhandler(404)
def page_not_found(err):
    return InputError.raise_error(str(err))


@app.route("/singup")
def singup():
    return render_template('singup.html')


@app.route('/user_added', methods=["GET", "POST"])
def user_added():
    try:
        new_user = UserCreate.read_user(request)
        Storage.add_user(new_user)
    except InputError as err:
        return InputError.raise_error(str(err))
    except MySQLError as err:
        return InputError.raise_error(str(err))
    except Exception as err:
        return InputError.raise_error(str(err))
    return render_template('post_added.html',
                           title='Welcome! you have signed up successfully. ',
                           post=new_user.username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_finded = Storage.select_user(username, password)
        if not user_finded:
            return InputError.raise_error("Check your username and password? If you don't have acount:Please SING UP!!!")

        session['log_in'] = username
        return redirect(url_for('check_status'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('log_in', None)
    return redirect(url_for('check_status'))


@app.route('/status')
@check_logged_in
def check_status():
    return render_template('check_logged_in.html', value='logged in', user=session['log_in'])


app.run(host='0.0.0.0', debug=True)
