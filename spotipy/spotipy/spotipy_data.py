from models import *


class SpotipyData:
    def __init__(self):
        self.tracks = []
        self.albums = []
        self.artists = []

    def add_track(self, track: Track):
        if track in self.tracks:
            print(f'track: {track} already exist in db')
        else:
            self.tracks.append(track)

    def add_album(self, album: Album):
        if album in self.albums:
            print(f'album: {album} already exist in db')
        else:
            self.albums.append(album)

    def add_artist(self, artist: Artist):
        if artist in self.artists:
            print(f'artist: {artist} already exist in db')
        else:
            self.artists.append(artist)
