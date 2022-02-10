from spotipy.spotipy_data import *
from users import *


def get_all_artists(spotipy_db: SpotipyData):
    return list(spotipy_db.artists)


def get_artist_albums(spotipy_db: SpotipyData, artist_id: str):
    for artist in spotipy_db.artists:
        if artist.id == artist_id:
            return list(artist.albums)
    else:
        print(f'artist id: {artist_id} does not exist')
        return []


def sort_parameter(track):
    return track.popularity


def ger_artist_top_tracks(spotipy_db: SpotipyData, artist_id: str, top=10):
    for artist in spotipy_db.artists:
        if artist.id == artist_id:
            top_tracks = list(artist.tracks).sort(key=sort_parameter, reverse=True)
            return top_tracks[:top]
    else:
        print(f'artist id: {artist_id} does not exist')
        return []


def get_album_tracks(spotipy_db: SpotipyData, album_id: str):
    for album in spotipy_db.albums:
        if album.id == album_id:
            return list(album.tracks)
    else:
        print(f'album id: {album_id} does not exist')
        return []
