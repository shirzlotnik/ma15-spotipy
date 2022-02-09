from spotipy.models import *


class LoginInfo:
    def __init__(self, username, password=None):
        self.username = username
        self.password = password


class User:
    def __init__(self, login_info: LoginInfo, premium=False):
        self.login_info = login_info
        self.playlist = []
        self._playlist_names = []
        self.premium = premium

    def add_playlist_decorator(self, add_playlist):
        def inner(playlist: Playlist):
            if not self.premium:
                if len(self.playlist) > 5:
                    print(f'you have reached the maximum amount of playlist, to add more consider upgrading to premium')
                    return

            if len(self.playlist) == 0:
                add_playlist(playlist)
            else:
                if playlist.name in self._playlist_names:
                    print(f'playlist {playlist.name} already exist')
                else:
                    add_playlist(playlist)

        return inner

    @add_playlist_decorator
    def add_playlist(self, playlist: Playlist):
        self.playlist.append(playlist)
        self._playlist_names.append(playlist.name)
        print(f'playlist {playlist.name} added successfully')
