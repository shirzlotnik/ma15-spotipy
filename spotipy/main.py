import json
import logging
import glob
from spotipy.config import *
from spotipy import extract, get_random_track
from spotipy.config import *
from flask_app import run
from spotipy_app import connect, add_playlist, add_track_to_playlist


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(filename=LOGS_FILE_PATH, level=LOG_LEVEL, format=LOG_FORMAT)

    spotipy_db = extract()
    spotipy_app = connect('shir', '1234')
    playlist_name = 'shir\'s playlist'
    track = get_random_track(spotipy_db)
    print(track.to_string())
    add_playlist(playlist_name, spotipy_app)
    add_track_to_playlist(playlist_name, track, spotipy_app)

    #run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
