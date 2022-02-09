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
    print(glob.glob(SONGS_PATH_GLOB))
    li = list(range(3))
    li2 = list(map(lambda x: x+3, li))
    print(li2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
