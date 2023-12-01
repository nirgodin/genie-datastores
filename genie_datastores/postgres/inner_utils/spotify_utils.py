from typing import Optional

from genie_datastores.postgres.consts.spotify_consts import ARTISTS, ID


def extract_artist_id(response: dict, field: str = ID) -> Optional[str]:
    artists = response.get(ARTISTS)

    if artists:
        return artists[0][field]
