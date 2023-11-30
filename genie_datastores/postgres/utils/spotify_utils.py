from typing import Optional

from postgres_client.consts.spotify_consts import ARTISTS, ID


def extract_artist_id(response: dict) -> Optional[str]:
    artists = response.get(ARTISTS)

    if artists:
        return artists[0][ID]
