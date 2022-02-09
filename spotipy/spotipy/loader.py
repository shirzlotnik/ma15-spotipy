import glob
from config import *
import logging
import json
from models import *


def load_track_files():
    json_files_paths = glob.glob(SONGS_PATH_GLOB)
    for json_file_path in json_files_paths:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)


def parse_json_track(json_data: dict):
    track_parameters = json_data[TRACK]
    track_album = track_parameters[ALBUM]
    track_artists = track_parameters[ARTISTS]
    track = Track(track_parameters['id'], track_parameters['name'], track_parameters['popularity'])


