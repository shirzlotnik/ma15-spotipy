from os import getenv
from app.config import *
from flask import Flask, redirect, url_for, request, session, render_template, flash
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
)
from users.users import *


def dump_users():
    users__x = [User('shir', '1234', ANONYMOUS), User('shir-premium', 'bdhj', PREMIUM), User('artist-shir', '4562143', ARTIST)]
    json_list = list(map(lambda user: user.to_json(), users__x))
    with open(USERS_JSON, encoding='utf-8', mode='w') as file:
        json.dump(json_list, file)


def load_users():
    with open(USERS_JSON, encoding='utf-8') as file:
        users = json.load(file)
    return users


def add_user(user):
    users = load_users()
    user_json = user.to_json()
    users.append(user_json)

    with open(USERS_JSON, encoding='utf-8', mode='w') as file:
        json.dump(users, file)


def check_if_user_exist(username):
    users = load_users()
    for user in users:
        if user[USERNAME] == username:
            return True
    return False


def find_user(username):
    users = load_users()
    for user in users:
        if user[USERNAME] == username:
            if ALBUMS in users.keys():
                return User(user[USERNAME], user[PASSWORD], user[TYPE], user[PLAYLISTS], user[ALBUMS])
            return User(user[USERNAME], user[PASSWORD], user[TYPE], user[PLAYLISTS])
    return None


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config["SECRET_KEY"] = getenv("SECRET_KEY", default="secret_key_example")

    login_manager = LoginManager(app)

    dump_users()
    users = load_users()

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    @app.route('/')
    def index():
        if 'username' in session:
            username = session['username']
            return 'Logged in as ' + username + '<br>' + \
                   "<b><a href = '/logout'>click here to log out</a></b>"

        return "You are not logged in <br><a href = '/login'></b>" + \
               "click here to log in</b></a>"

    @app.route("/login", methods=["GET", "POST"])
    def login_page():
        if request.method == "POST":
            name = request.form.get('name')
            password = request.form.get('password')
            if isinstance(password, str):
                return str(password)
            if check_if_user_exist(name):
                user = find_user(name)
                if user is None:
                    print('user not found')
                else:
                    if user[PASSWORD] == password:
                        return redirect(url_for('spotipy_user', username=user[USERNAME]))
        else:
            name = request.args.get('name')
            return render_template(LOGIN_HTML)
        return 'error'

        #return render_template(LOGIN_HTML)

    @app.route('/spotipy/<username>')
    def spotipy_user(username):
        return 'hello' + username

    @app.route('/signup', methods=['GET', 'POST'])
    def signup_page():
        signup_form = request.form
        # POST: Sign user in
        if request.method == 'POST':
            # Get Form Fields
            name = request.form.get('name')
            password = request.form.get('password')
            rewritten_password = request.form.get('rewritten_password')
            type = request.form.get('subscription')
            if password != rewritten_password:
                flash('the passwords do not match')
                return redirect(url_for('signup_page'))
            if check_if_user_exist(name, users):
                flash('A user exists with that email address.')
                return redirect(url_for('signup_page'))

            else:
                new_user = User(name, password, type)
                add_user(new_user)

            return redirect(url_for('login_page'))
        # GET: Serve Sign-up page
        return render_template(
            SIGNUP_HTML,
            title='Create an Account | Flask-Login Tutorial.',
            template='signup-page',
            body="Sign up for a user account."
        )







    @app.route('/abc', methods=['GET', 'POST'])
    def abc():
        if request.method == 'GET':
            return '''
                   <form action='login' method='POST'>
                    <input type='text' name='userntytyame' id='usxxxxername' placeholder='username'/>
                    <input type='password' name='password' id='password' placeholder='password'/>
                    <input type='submit' name='submit'/>
                   </form>
                   '''

        username = request.form[USERNAME]
        if request.form[PASSWORD] == users[username]['password']:
            user = User()
            user.id = username
            login_user(user)
            return redirect(url_for('protected'))

        return 'Bad login'

    @app.route('/protected')
    @login_required
    def protected():
        return 'Logged in as: ' + current_user.id

    return app
