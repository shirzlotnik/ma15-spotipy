from typing import List

class Track:
    def __init__(self, id: str, name: str, popularity: int):
        self.id = id
        self.name = name
        self.popularity = popularity


class Album:
    def __init__(self, id: str, name: str, tracks: List[Track]):
        self.id = id
        self.name = name
        self.tracks = tracks


class Artist:
    def __init__(self, id: str, name: str, albums: List[Album]):
        self.id = id
        self.name = name
        self.albums = albums
