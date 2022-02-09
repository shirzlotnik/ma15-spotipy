from typing import List
from spotipy.config import *

class Artist:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.albums = []
        self.genre = ''
        self.tracks = []

    def add_album(self, album):
        self.albums.append(album)

    def add_track(self, track):
        self.tracks.append(track)

    def to_string(self):
        str = f'Artist - id: {self.id}, name: {self.name}\n'
        for album in self.albums:
            str += f'\tAlbum - id: {album.id}, name: {album.name}\n'

        return str


class Album:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.tracks = []

    def add_track(self, track_id):
        self.tracks_ids.append(track_id)

    def to_string(self):
        str = f'Album - id: {self.id}, name: {self.name}\n'
        for track in self.tracks:
            str += f'\tTrack - id:{track.id}, name: {track.name}\n'

        return str


class Track:
    def __init__(self, id: str, name: str, popularity: int, album: Album, artists: List[Artist]):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.album = album
        self.artists = artists

    def to_string(self):
        str = f'Track - id: {self.id}, name: {self.name}, popularity: {self.popularity}\n'
        str += f'\tAlbum - id{self.album.id}, name: {self.album.name}\n'
        for artist in self.artists:
            str += f'\tArtist - id: {artist.id}, name: {artist.name}\n'

        return str


class Playlist:
    def __init__(self, name, tracks=[]):
        self.tracks = tracks
        self.name = name
