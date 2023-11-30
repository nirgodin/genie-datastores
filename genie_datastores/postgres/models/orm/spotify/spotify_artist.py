from typing import List, Optional

from sqlalchemy import Column, String, ARRAY, Enum, TIMESTAMP, Boolean

from postgres_client.consts.orm_consts import SPOTIFY_ARTISTS_TABLE, ID
from postgres_client.consts.spotify_consts import NAME, GENRES
from postgres_client.models.enum.data_source import DataSource
from postgres_client.models.enum.gender import Gender
from postgres_client.models.orm.spotify.base_spotify_orm_model import BaseSpotifyORMModel


class SpotifyArtist(BaseSpotifyORMModel):
    __tablename__ = SPOTIFY_ARTISTS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    birth_date = Column(TIMESTAMP)
    death_date = Column(TIMESTAMP)
    facebook_name = Column(String)
    gender = Column(Enum(Gender))
    gender_source = Column(Enum(DataSource))
    genres = Column(ARRAY(String))
    instagram_name = Column(String)
    is_israeli = Column(Boolean)
    is_lgbtq = Column(Boolean)
    primary_genre = Column(String)
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
