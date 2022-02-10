class ReachedPlaylistsLimit(ValueError):
    def __init__(self):
        pass


class PlaylistAlreadyExist(NameError):
    def __init__(self):
        pass


class ReachedTrackLimit(ValueError):
    def __init__(self):
        pass


class DBConnectionError(ConnectionError):
    def __init__(self):
        pass


class UserNotFound(NameError):
    def __init__(self):
        pass


class PlaylistNotFound(ModuleNotFoundError):
    def __init__(self):
        pass




