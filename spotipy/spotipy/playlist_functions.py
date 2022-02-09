from models import *
import logging
from users.users import *


def playlist_validation_for_user(playlist: Playlist):
    logging.debug('checking user authentication')
    if not self.premium:
        if len(self.playlist) > 5:
            print(f'you have reached the maximum amount of playlist, to add more consider upgrading to premium')
            return False

        if len(playlist.tracks) > 20:
            print(f'a playlist can have up to 20 tracks, to add more consider upgrading to premium')
            return False

    return True

def add_playlist_decorator(self, add_playlist):
    def inner(playlist: Playlist):
        if self.playlist_validation_for_user(playlist):
            if playlist.name in self._playlist_names:
                print(f'playlist {playlist.name} already exist')
            else:
                add_playlist(playlist)

    return inner

@add_playlist_decorator
def add_playlist(self, playlist: Playlist):
    logging.debug('adding playlist')
    self.playlist.append(playlist)
    self._playlist_names.append(playlist.name)
    print(f'playlist {playlist.name} added successfully')

