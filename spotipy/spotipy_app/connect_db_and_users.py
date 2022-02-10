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
            if user[USERNAME] is self.username:
                if user[PASSWORD] is self.password:
                    self.current_user = User(user[USERNAME], user[PASSWORD], user[TYPE], user[PLAYLISTS], user[ALBUMS])
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

        connection_user = connection.user.username
        connection_password = connection.user.password
        for user in self.users:
            if user.username == connection_user:
                if user.password == connection_password:
                    self.current_connection = connection
                    self.connected = True
                    logging.debug('successfully connected to user')
                    print(f'hello, {self.username}')
                else:
                    print(f'password for user: {self.username} is incorrect')
                    logging.exception('user entered wrong password')
            else:
                print(f'could not find user:{self.username}')
                logging.error(f'user {user.username} does not exist in db')





