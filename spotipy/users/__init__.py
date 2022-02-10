from app.app import load_users
from users.users import *
from users.search import *
from users.config import *


def check_if_artist_has_user(artist_name):
    users = load_users()
    for user in users:
        if user.username == artist_name:
            return user
    return None


def update_artist_users(spotipy_db: SpotipyData):
    from app.app import load_users
    users = load_users()
    for artist in spotipy_db.artists:
        artist_user = check_if_artist_has_user(artist.name, spotipy_db)
        if artist_user is None:
            #create_acount
            pass
        else:
            if artist_user.type is ARTIST:
                artist_user.albums = artist.albums


def get_all_artists(user: User, spotipy_db: SpotipyData):
    if user.type is ANONYMOUS:
        list(spotipy_db.artists)[:ANSWERS_LIMIT]
    return list(spotipy_db.artists)


def get_artist_albums(user:User, spotipy_db: SpotipyData, artist_id: str):
    for artist in spotipy_db.artists:
        if artist.id == artist_id:
            if user.type is ANONYMOUS:
                return list(artist.albums)[:ANSWERS_LIMIT]
            return list(artist.albums)
    else:
        print(f'artist id: {artist_id} does not exist')
        return []


def sort_parameter(track):
    return track.popularity


def ger_artist_top_tracks(user:User, spotipy_db: SpotipyData, artist_id: str, top=10):
    for artist in spotipy_db.artists:
        if artist.id == artist_id:
            top_tracks = list(artist.tracks).sort(key=sort_parameter, reverse=True)
            if user.type is ANONYMOUS:
                return top_tracks[:ANSWERS_LIMIT]
            return top_tracks[:top]

    else:
        print(f'artist id: {artist_id} does not exist')
        return []


def get_album_tracks(user:User, spotipy_db: SpotipyData, album_id: str):
    for album in spotipy_db.albums:
        if album.id == album_id:
            if user.type is ANONYMOUS:
                return list(album.tracks)[:ANSWERS_LIMIT]
            return list(album.tracks)

    else:
        print(f'album id: {album_id} does not exist')
        return []
