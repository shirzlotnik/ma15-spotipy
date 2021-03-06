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

    def get_tracks(self):
        for album in self.albums:
            self.tracks += album.tracks

    def to_string(self):
        str = f'Artist - id: {self.id}, name: {self.name}\n'
        for album in self.albums:
            str += '\t' + album.to_string() + '\n'

        return str


class Album:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.tracks = []
        self.artists = []

    def add_track(self, track):
        self.tracks.append(track)
        self.artists += track.artists

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
    def __init__(self, name, limit=True):
        self.tracks = []
        self.name = name
        self.limit = limit

    def add_track(self, track):
        from users.exceptions import ReachedTrackLimit
        if self.limit:
            if len(self.tracks) > TRACKS_LIMIT:
                print('you have reach the maximum amount of tracks in playlist, to add more consider upgrading to '
                      'premium')
                logging.exception('user try to add invalid number of tracks to playlist')
                raise ReachedTrackLimit

        self.tracks.append(track)

    def to_string(self):
        str = f'Playlist -\nname: {self.name}\n'
        for track in self.tracks:
            str += f'\t{track.to_string()}'
        if self.limit:
            str += f'tracks limit: {TRACKS_LIMIT}\n'

        return str
