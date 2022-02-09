from typing import List

class Track:
    def __init__(self, id: str, name: str, popularity: int):
        self.id = id
        self.name = name
        self.popularity = popularity


class Album:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class Artist:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
