import json
import logging
import glob
from spotipy.config import *
from spotipy import extract
from spotipy.config import *
from flask_app import run


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(filename=LOGS_FILE_PATH, level=LOG_LEVEL, format=LOG_FORMAT)

    extract()
    run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
