import json
import logging
import glob
from spotipy.config import *
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    file_path = '/Users/shirzlotnik/songs/song_0oHTvb0EVeYTUc0zscZphb.json'
    with open(file_path, 'r') as file:

        data = json.load(file)

    print(data)
    print(glob.glob(SONGS_PATH_GLOB))
    li = ['a', 'b', 'c']
    li4 = []
    li2 = list(map(lambda x: x+'r', li))
    for i in li:
        li4.append(i)
    print(li2)
    print(li4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
