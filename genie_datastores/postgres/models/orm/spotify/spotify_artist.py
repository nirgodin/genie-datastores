from typing import List, Optional

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_ARTISTS_TABLE, ID
from genie_datastores.postgres.consts.spotify_consts import NAME, GENRES
from genie_datastores.postgres.models.orm.spotify.base_spotify_orm_model import BaseSpotifyORMModel


class SpotifyArtist(BaseSpotifyORMModel):
    __tablename__ = SPOTIFY_ARTISTS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    about = Column(String)
    facebook_name = Column(String)
    genres = Column(ARRAY(String))
    instagram_name = Column(String)
    twitter_name = Column(String)
    wikipedia_language = Column(String)
    wikipedia_name = Column(String)

    @classmethod
    def from_spotify_response(cls, response: dict) -> "SpotifyArtist":
        return cls(
            id=response[ID],
            name=response[NAME],
            genres=cls._extract_genres(response)
        )

    @staticmethod
    def _extract_genres(response: dict) -> Optional[List[str]]:
        genres = response.get(GENRES)
        return genres if genres else None
