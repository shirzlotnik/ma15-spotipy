import logging
from typing import List
from spotipy.models import *

from spotipy.extract_and_parse import *


class SpotipyData:
    def __init__(self):
        self.tracks = {}
        self.albums = {}
        self.artists = {}

    def add_track(self, track: Track):
        if track.id in self.tracks.keys():
            print(f'track: {track} already exist in db')
            logging.exception('user enter an existing track')
        else:
            self.tracks[track.id] = track
            logging.debug(f'successfully added track {track}')

    def add_album(self, album: Album):
        if album.id in self.albums.keys():
            print(f'album: {album} already exist in db')
        else:
            self.albums[album.id] = album
            logging.debug(f'successfully added album {album}')

    def add_artists(self, artists: List[Artist]):
        for artist in artists:
            if artist.id not in self.artists.keys():
                self.artists[artist.id] = artist
                logging.debug(f'successfully added artist {artist}')

    def process_albums(self):
        for track in self.tracks.values():
            if track.album.id in self.albums.keys():
                self.albums[track.album.id].add_track(track)

    def process_artists(self):
        for album in self.albums.values():
            for artist in album.artists:
                if artist.id in self.artists.keys():
                    self.artists[artist.id].add_album(album)
