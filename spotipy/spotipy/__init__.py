from spotipy.config import *
import logging


def extract():
    from spotipy.extract_and_parse import extract
    from spotipy.spotipy_data import SpotipyData

    spotipy_db = SpotipyData()

    logging.info('extracting data into spotipy db')
    extract(spotipy_db)
    logging.info('adding values to albums')
    spotipy_db.process_albums()
    logging.info('adding values to artists')
    spotipy_db.process_artists()



    for track in spotipy_db.tracks.values():
        print(track.to_string())
'''
    for album in spotipy_db.albums.values():
        print(album.to_string())

    for artist in spotipy_db.artists.values():
        print(artist.to_string())
'''