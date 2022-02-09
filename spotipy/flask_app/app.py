import json
from os import getenv
from flask_app.config import *
from flask import Flask, redirect, url_for, request, session
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,)

from users.users import *


def dump_users():
    users__x = [User('shir', '1234'), User('shir-premium', 'bdhj', PREMIUM), ArtistUser('artist-shir', '4562143')]
    json_list = list(map(lambda user: user.to_json(), users__x))
    with open("/Users/shirzlotnik/spotipy/spotipy/spotipy/flask_app/users.json", encoding='utf-8', mode='w') as file:
        json.dump(json_list, file)


def load_users():
    with open("/Users/shirzlotnik/spotipy/spotipy/spotipy/flask_app/users.json", encoding='utf-8') as file:
        users = json.load(file)
    return users


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = getenv("SECRET_KEY", default="secret_key_example")

    login_manager = LoginManager(app)

    dump_users()
    users = load_users()

    def find_user(username):
        for user in users:
            if user[USERNAME] == username:
                if user[TYPE] is ANONYMOUS:
                    return User(user[USERNAME], user[PASSWORD])
                elif user[TYPE] is PREMIUM:
                    return User(user[USERNAME], user[PASSWORD], PREMIUM)
                else:
                    return ArtistUser(user[USERNAME], user[PASSWORD])

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return '''
                   <form action='login' method='POST'>
                    <input type='text' name='username' id='username' placeholder='username'/>
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

    @app.route('/')
    def index():
        if 'username' in session:
            username = session['username']
            return 'Logged in as ' + username + '<br>' + \
                   "<b><a href = '/logout'>click here to log out</a></b>"

        return "You are not logged in <br><a href = '/login'></b>" + \
               "click here to log in</b></a>"

    return app