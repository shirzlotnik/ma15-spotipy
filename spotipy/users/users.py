import logging

from spotipy.models import *
from users.config import *
from users.exceptions import *


class User:
    def __init__(self, username, password, user_type, playlists=[], albums=[]):
        self.username = username
        self.password = password
        self.type = user_type
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
                raise PlaylistAlreadyExist

        playlist = None
        if self.type == ANONYMOUS:
            playlist = Playlist(name)
        elif self.type == PREMIUM:
            playlist = Playlist(name, False)

        if playlist is not None:
            self.playlists.append(playlist)
            logging.info('playlist added successfully')
        else:
            logging.error(f'problem with playlist {name}')

    def add_track_to_playlist(self, name, track: Track):
        for playlist in self.playlists:
            if playlist.name is name:
                logging.debug('trying to add track to playlist')
                try:
                    playlist.add_track(track)
                except ReachedTrackLimit:
                    raise ReachedTrackLimit
            else:
                logging.error('playlist not found')
                raise PlaylistNotFound
        logging.info(f'added track {track} to playlist {name} successfully')


