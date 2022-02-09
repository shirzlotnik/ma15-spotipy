from models import *
from extract_and_parse import *
import glob
import json


class SpotipyData:
    def __init__(self):
        self.tracks = []
        self.albums = []
        self.artists = []

    def extract(self):
        json_files_paths = glob.glob(SONGS_PATH_GLOB)
        for json_file_path in json_files_paths:
            with open(json_file_path, 'r') as json_file:
                logging.debug('reading json file from directory')
                data = json.load(json_file)
                track, album, artists = parse_json_track(data)
                self._add_track(track)
                self._add_album(album)
                for artist in artists:
                    self._add_artist(artist)

    def _add_track(self, track: Track):
        if track in self.tracks:
            print(f'track: {track} already exist in db')
        else:
            self.tracks.append(track)

    def _add_album(self, album: Album):
        if album in self.albums:
            print(f'album: {album} already exist in db')
        else:
            self.albums.append(album)

    def _add_artist(self, artist: Artist):
        if artist in self.artists:
            print(f'artist: {artist} already exist in db')
        else:
            self.artists.append(artist)
