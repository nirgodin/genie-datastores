from datetime import datetime
from typing import Optional, List

from genie_common.utils import safe_nested_get, to_datetime
from sqlalchemy import String, Column, ARRAY, TIMESTAMP

from genie_datastores.postgres.consts.datetime_consts import SHAZAM_DATETIME_FORMATS
from genie_datastores.postgres.consts.orm_consts import SHAZAM_ARTISTS_TABLE
from genie_datastores.postgres.consts.shazam_consts import ATTRIBUTES, ARTIST_BIO, GENRE_NAMES, ORIGIN, DATA, \
    BORN_OR_FORMED, VIEWS, SIMILAR_ARTISTS
from genie_datastores.postgres.consts.spotify_consts import ID, NAME
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class ShazamArtist(BaseORMModel):
    __tablename__ = SHAZAM_ARTISTS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    about = Column(String)
    birth_date = Column(TIMESTAMP)
    genres = Column(ARRAY(String))
    origin = Column(String)
    similar_artists = Column(ARRAY(String))

    @classmethod
    def from_shazam_response(cls, response: dict) -> Optional["ShazamArtist"]:
        artist = cls._extract_artist_from_response(response)
        if artist:
            return cls(
                id=artist[ID],
                name=safe_nested_get(artist, [ATTRIBUTES, NAME]),
                about=safe_nested_get(artist, [ATTRIBUTES, ARTIST_BIO]),
                birth_date=cls._extract_birth_date(artist),
                genres=safe_nested_get(artist, [ATTRIBUTES, GENRE_NAMES]),
                origin=safe_nested_get(artist, [ATTRIBUTES, ORIGIN]),
                similar_artists=cls._extract_related_artists_ids(artist)
            )

    @staticmethod
    def _extract_artist_from_response(response: dict) -> Optional[dict]:
        data = response.get(DATA)

        if data:
            return data[0]

    @staticmethod
    def _extract_birth_date(artist: dict) -> Optional[datetime]:
        birth_date = safe_nested_get(artist, [ATTRIBUTES, BORN_OR_FORMED])

        if birth_date is not None:
            return to_datetime(birth_date, SHAZAM_DATETIME_FORMATS)

    @staticmethod
    def _extract_related_artists_ids(artist: dict) -> Optional[List[str]]:
        similar_artists_records = safe_nested_get(artist, [VIEWS, SIMILAR_ARTISTS, DATA])

        if similar_artists_records:
            return [record[ID] for record in similar_artists_records]
