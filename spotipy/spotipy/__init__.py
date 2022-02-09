from spotipy.config import *


def extract():
    from spotipy.extract_and_parse import extract, parse_json_track
    from spotipy.spotipy_data import SpotipyData

    spotipy_db = SpotipyData()

    extract(spotipy_db)

    for track in spotipy_db.tracks.values():
        print(track.to_string())

    for album in spotipy_db.albums.values():
        print(album.to_string())

    for artist in spotipy_db.artists.values():
        print(artist.to_string())