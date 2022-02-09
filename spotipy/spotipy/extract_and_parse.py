from config import *
from models import *
from spotipy_data import *
import logging


def parse_json_track(json_data: dict):
    logging.debug('parsing json to track, album, artist objects')
    track_parameters = json_data[TRACK]
    track_album = track_parameters[ALBUM]
    track_artists = track_parameters[ARTISTS]
    track = Track(track_parameters[ID], track_parameters[NAME], track_parameters[POPULARITY])
    album = Album(track_album[ID], track_album[NAME])
    artists = list(map(lambda artist: Artist(artist[ID], artist[NAME]), track_artists))

    return update_models_parameters(track, album, artists)


def update_models_parameters(track: Track, album: Album, artists: List[Artist]):
    logging.debug('updating track, album, artist objects')
    track.add_album(album)
    track.add_artists(artists)

    album.add_track(track)

    for artist in artists:
        artist.add_album(album)

    return track, album, artists




