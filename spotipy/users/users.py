from spotipy.models import *
import logging
from spotipy.spotipy_data import *


class LoginInfo:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password


class User:
    def __init__(self, login_info: LoginInfo, premium=False):
        self.login_info = login_info
        self.playlist = []
        self.playlist_names = []
        self.premium = premium


class ArtistUser(User):
    def __init__(self, login_info: LoginInfo):
        super.__init__(login_info, True)
        self.albums = []
        self.albums_names = []

    def add_artist_albums(self, spotipy: SpotipyData):
        logging.debug('adding artist user its albums')
        for artist in spotipy.artists:
            if artist.name == self.login_info.username:
                self.albums += artist.albums

