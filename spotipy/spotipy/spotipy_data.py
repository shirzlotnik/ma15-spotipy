from spotipy.models import *
from spotipy.extract_and_parse import *
import glob
import logging
import json
from collections import defaultdict
from typing import List


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
            if artist.id in self.artists.keys():
                print(f'artist: {artist} already exist in db')
            else:
                self.artists[artist.id] = artist
                logging.debug(f'successfully added artist {artist}')

    #def process_data(self):

    def process_albums_data(self):
        for track in self.tracks.values():
            if track.album_id in self.albums.keys():
                Album(self.albums[track.album_id]).add_track(track.id)
