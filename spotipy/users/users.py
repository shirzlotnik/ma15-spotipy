from spotipy.models import *
import logging
from spotipy.spotipy_data import *
from users.config import *
from spotipy.models import *
import logging


class User:
    def __init__(self, username, password, type, playlists=[], albums=[]):
        self.username = username
        self.password = password
        self.type = type
        self.playlists = playlists
        self.albums = albums

    def to_json(self):
        if self.type is not ARTIST:
            json_obj = {USERNAME: self.username, PASSWORD: self.password, TYPE: self.type, PLAYLISTS: self.playlists}
        else:
            json_obj = {USERNAME: self.username, PASSWORD: self.password, TYPE: self.type, PLAYLISTS: self.playlists,
                        ALBUMS: self.albums}

        return json_obj

    def create_playlist(self, name):
        for playlist in self.playlists:
            if playlist.name is name:
                logging.error('playlist name already exists')
                return

        if self.type is ANONYMOUS:
            playlist = Playlist(name)
        elif self.type is PREMIUM:
            playlist = Playlist(name, False)

        self.playlists.append(playlist)

    def add_track_to_playlist(self, name, track):
        for playlist in self.playlists:
            if playlist.name is name:
                playlist.add_track(track)


