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
    from spotipy.models import Playlist
    from users.exceptions import ReachedPlaylistsLimit

    try:
        spotipy_app.add_playlist_to_user(playlist)
    except PlaylistAlreadyExist:
        print(f'type: {PlaylistAlreadyExist} description: playlist {playlist.name} already exists')
        return
    except ReachedPlaylistsLimit:
        print(f'type: {ReachedPlaylistsLimit} description: you have reached your playlists max capacity')
        return

    logging.debug('playlist added successfully')
