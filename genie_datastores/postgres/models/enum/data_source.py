from enum import Enum


class DataSource(Enum):
    GENERAL_WIKIPEDIA = "general_wikipedia"
    GENIUS = "genius"
    GOOGLE_IMAGES = "google_images"
    ISRAELI_WIKIPEDIA = "israeli_wikipedia"
    MANUAL_TAGGING = "manual_tagging"
    MUSIXMATCH = "musixmatch"
    OPENAI = "openai"
    SHAZAM = "shazam"
    SPOTIFY_EQUAL_PLAYLISTS = "spotify_equal_playlists"
    SPOTIFY_IMAGES = "spotify_images"
    CHARTS = "charts"
