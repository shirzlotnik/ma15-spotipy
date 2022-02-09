from models import *
import logging
from users.users import *


def playlist_validation_for_user(user: User, playlist: Playlist):
    logging.debug('checking user authentication')
    if not user.premium:
        if len(user.playlist) > 5:
            print(f'you have reached the maximum amount of playlist, to add more consider upgrading to premium')
            return False

        if len(playlist.tracks) > 20:
            print(f'a playlist can have up to 20 tracks, to add more consider upgrading to premium')
            return False

    return True


def add_playlist_decorator(add_playlist):
    def inner(user, playlist: Playlist):
        if playlist_validation_for_user(user, playlist):
            if playlist.name in user.playlist_names:
                print(f'playlist {playlist.name} already exist')
                logging.exception('user entered invalid playlist name')
            else:
                add_playlist(playlist)

    return inner


@add_playlist_decorator
def add_playlist(user, playlist: Playlist):
    logging.debug('adding playlist')
    user.playlist.append(playlist)
    user.playlist_names.append(playlist.name)
    print(f'playlist {playlist.name} added successfully')

