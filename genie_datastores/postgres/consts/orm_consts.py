from genie_datastores.postgres.consts.spotify_consts import ID

# Spotify
SPOTIFY_TRACKS_TABLE = "spotify_tracks"
SPOTIFY_ARTISTS_TABLE = "spotify_artists"

SPOTIFY_TRACKS_ID = f"{SPOTIFY_TRACKS_TABLE}.{ID}"
SPOTIFY_ARTISTS_ID = f"{SPOTIFY_ARTISTS_TABLE}.{ID}"

# Shazam
SHAZAM_TRACKS_TABLE = "shazam_tracks"
SHAZAM_ARTISTS_TABLE = "shazam_artists"

SHAZAM_TRACK_ID = f"{SHAZAM_TRACKS_TABLE}.{ID}"
SHAZAM_ARTIST_ID = f"{SHAZAM_ARTISTS_TABLE}.{ID}"

# Cases
CASES_TABLE = "cases"
CASES_TABLE_ID = f"{CASES_TABLE}.{ID}"
