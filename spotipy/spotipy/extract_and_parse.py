from spotipy.config import *
from spotipy.models import *
from spotipy.spotipy_data import SpotipyData
import glob
from spotipy.spotipy_data import *
import logging
import json


def extract(spotipy_db):
    logging.info('extracting data from songs directory')
    json_files_paths = glob.glob(SONGS_PATH_GLOB)
    for json_file_path in json_files_paths:
        with open(json_file_path, 'r') as json_file:
            logging.debug('reading json file from directory')
            data = json.load(json_file)
            track, album, artists = parse_json_track(data)
            spotipy_db.add_track(track)
            spotipy_db.add_album(album)
            spotipy_db.add_artists(artists)


def parse_json_track(json_data: dict):
    logging.debug('parsing json to track, album, artist objects')
    track_data = json_data[TRACK]
    album = Album(track_data[ID], track_data[NAME])
    artists = list(map(lambda x: Artist(x[ID], x[NAME]), track_data[ARTISTS]))
    track = Track(track_data[ID], track_data[NAME], track_data[POPULARITY], album, artists)

    return track, album, artists




