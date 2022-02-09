from typing import List


class Artist:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


class Album:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)


class Track:
    def __init__(self, id: str, name: str, popularity: int):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.album = None
        self.artists = []

    def add_album(self, album: Album):
        self.album = album

    def add_artists(self, artists: List[Artist]):
        self.artists = artists
