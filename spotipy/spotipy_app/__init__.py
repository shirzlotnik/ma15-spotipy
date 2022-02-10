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
    return spotipy_app


def add_playlist(playlist, spotipy_app: SpotipyApp):
    is_added = spotipy_app.add_playlist_to_user(playlist)
    if is_added:
        logging.info('playlist added successfully')
    else:
        logging.exception('could not add playlist')


def add_track_to_playlist(name, track, spotipy_app: SpotipyApp):
    is_added = spotipy_app.add_track_to_playlist(name, Track)
    if is_added:
        logging.info('track added successfully')
    else:
        logging.exception('could not add track to playlist')