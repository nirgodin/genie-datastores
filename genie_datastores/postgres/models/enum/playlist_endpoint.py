from enum import Enum


class PlaylistEndpoint(Enum):
    CONFIGURATION = "configuration"
    EXISTING_PLAYLIST = "existingPlaylist"
    FOR_YOU = "forYou"
    MERGE_PLAYLISTS = "mergePlaylists"
    PHOTO = "photo"
    PROMPT = "prompt"
    WRAPPED = "wrapped"
