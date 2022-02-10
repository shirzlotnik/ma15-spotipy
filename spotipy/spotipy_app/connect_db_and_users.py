from spotipy.spotipy_data import *
from users.users import *
from users.config import *
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





