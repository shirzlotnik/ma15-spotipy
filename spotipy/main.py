import json
import logging
import glob

import app.app
from spotipy.config import *
from spotipy import extract, get_random_track
from spotipy.config import *
from app import run
from spotipy_app import connect, add_playlist, add_track_to_playlist
from consolemenu import *
from consolemenu.items import *
from os import system


if __name__ == '__main__':
    logging.basicConfig(filename=LOGS_FILE_PATH, level=LOG_LEVEL, format=LOG_FORMAT)

    spotipy_db = extract()
    spotipy_app = connect('shir', '1234')
    playlist_name = 'shir\'s playlist'
    track = get_random_track(spotipy_db)
    print(track.to_string())
    add_playlist(playlist_name, spotipy_app)
    add_track_to_playlist(playlist_name, track, spotipy_app)


    run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
