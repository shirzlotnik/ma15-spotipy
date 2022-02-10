from spotipy_app.connect_db_and_users import *


def connect(username, password):
    from spotipy.spotipy_data import SpotipyData
    from flask_app.app import load_users
    spotipy_db = SpotipyData()
    users = load_users()
    connection = Connection(username, password)
    connection.valid_user(users)
    spotipy_app = SpotipyApp(spotipy_db, users)
    spotipy_app.connect(connection)
