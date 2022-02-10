from spotipy.spotipy_data import *
from users.users import *
from users.config import *
from users.exceptions import *
import logging


class Connection:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.current_user = None

    def valid_user(self, users):
        for user in users:
            if user[USERNAME] == self.username:
                if user[PASSWORD] == self.password:
                    if ALBUMS in user.keys():
                        self.current_user = User(user[USERNAME], user[PASSWORD], user[TYPE], user[PLAYLISTS], user[ALBUMS])
                    else:
                        self.current_user = User(user[USERNAME], user[PASSWORD], user[TYPE], user[PLAYLISTS])

                    logging.debug('successfully validation to user')

                else:
                    logging.exception('password does not much db')
            else:
                logging.exception('user not found')


class SpotipyApp:
    def __init__(self, spotipy_db: SpotipyData, users):
        self.spotipy_db = spotipy_db
        self.users = users
        self.connected = False
        self.current_connection = None
        self.current_user: User
        self.current_user = None

    def connect(self, connection: Connection):
        if connection.current_user is None:
            logging.error('connection error, user not found')
            print(f'invalid connection')
            return

        connection_user = connection.username
        connection_password = connection.password
        for user in self.users:
            if user[USERNAME] == connection_user:
                if user[PASSWORD] == connection_password:
                    self.current_connection = connection
                    self.current_user = self.current_connection.current_user
                    self.connected = True
                    logging.debug('successfully connected to user')
                    print(f'hello, {connection_user}')
                    return
                else:
                    print(f'password for user: {connection_user} is incorrect')
                    logging.exception('user entered wrong password')
            else:
                print(f'could not find user:{connection_user}')
                logging.error(f'user {connection_user} does not exist in db')

    def add_playlist_to_user(self, playlist_name):
        if self.connected:
            if self.current_user is not None:
                logging.debug('trying to add playlist')
                try:
                    self.current_user.create_playlist(playlist_name)
                except PlaylistAlreadyExist:
                    logging.exception('playlist already exists')
                    print(f'type: {PlaylistAlreadyExist} description: playlist {playlist_name} already exists')
                    return False
                except ReachedPlaylistsLimit:
                    logging.exception('reached playlists limit')
                    print(f'type: {ReachedPlaylistsLimit} description: you have reached your playlists max capacity')
                    return False
            else:
                logging.exception('user not found')
                print(f'user not found')
                return False
        else:
            print(f'connection not found')
            return False

        return True

    def add_track_to_playlist(self, name, track: Track):
        logging.debug('trying to add track to a playlist')
        try:
            self.current_user.add_track_to_playlist(name, track)
        except ReachedTrackLimit:
            print(f'type: {ReachedTrackLimit}, description: you have reached max track for playlist')
            return False
        except PlaylistNotFound:
            print(f'type: {PlaylistNotFound}, description: could not find playlist {name}')
            return False

        logging.info('track added successfully')
        return True






