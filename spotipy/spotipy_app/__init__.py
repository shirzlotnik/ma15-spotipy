from spotipy_app.connect_db_and_users import *


def connect(username, password):
    from spotipy.spotipy_data import SpotipyData
    from app.app import load_users
    spotipy_db = SpotipyData()
    users = load_users()
    connection = Connection(username, password)
    connection.valid_user(users)
    spotipy_app = SpotipyApp(spotipy_db, users)
    spotipy_app.connect(connection)
    return spotipy_app


def add_playlist(playlist_name, spotipy_app: SpotipyApp):
    is_added = spotipy_app.add_playlist_to_user(playlist_name)
    if is_added:
        logging.info('playlist added successfully')
    else:
        logging.exception('could not add playlist')

    '''
    users_playlists = list(spotipy_app.current_user.playlists)
    for playlist in users_playlists:
        print(playlist.to_string())

    '''


def add_track_to_playlist(playlist_name, track, spotipy_app: SpotipyApp):
    is_added = spotipy_app.add_track_to_playlist(playlist_name, track)
    if is_added:
        logging.info('track added successfully')
    else:
        logging.exception('could not add track to playlist')

    '''
    users_playlists = list(spotipy_app.current_user.playlists)
    for playlist in users_playlists:
        print(playlist.to_string())
    '''
