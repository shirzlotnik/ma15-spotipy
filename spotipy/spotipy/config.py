import logging

SONGS_PATH = '/Users/shirzlotnik/songs'
SONGS_PATH_GLOB = '/Users/shirzlotnik/songs/*.json'

LOGS_FILE_PATH = 'spotipy.log'
LOGS_ENCODING = 'utf-8'
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = '%(asctime)s - at %(name)s - %(levelname)s: %(message)s'

TRACK = 'track'
ALBUM = 'album'
ARTISTS = 'artists'
NAME = 'name'
ID = 'id'
POPULARITY = 'popularity'

TRACKS_LIMIT = 20
PLAYLISTS_LIMIT = 5