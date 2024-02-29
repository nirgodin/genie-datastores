from enum import Enum


class PlaylistEndpoint(Enum):
    CONFIGURATION = "configuration"
    EXISTING_PLAYLIST = "existingPlaylist"
    FOR_YOU = "forYou"
    PHOTO = "photo"
    PROMPT = "prompt"
    WRAPPED = "wrapped"
