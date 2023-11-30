from typing import Optional

from sqlalchemy import Column, String, ForeignKey, ARRAY

from postgres_client import BaseORMModel
from postgres_client.consts.audio_features_consts import KEY
from postgres_client.consts.orm_consts import SHAZAM_TRACKS_TABLE, SHAZAM_ARTIST_ID
from postgres_client.consts.shazam_consts import ADAM_ID, TITLE, PRIMARY, SECTIONS, METADATA, TEXT, LABEL
from postgres_client.consts.spotify_consts import ARTISTS, GENRES
from postgres_client.tools import ShazamWritersExtractor
from postgres_client.utils.dict_utils import safe_nested_get


class ShazamTrack(BaseORMModel):
    __tablename__ = SHAZAM_TRACKS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    artist_id = Column(String, ForeignKey(SHAZAM_ARTIST_ID), nullable=False)
    name = Column(String, nullable=False)
    label = Column(String)
    writers = Column(ARRAY(String))
    primary_genre = Column(String)

    @classmethod
    def from_shazam_response(cls, response: dict) -> Optional["ShazamTrack"]:
        artist_id = cls._extract_artist_id(response)
        if artist_id:
            return cls(
                id=response[KEY],
                artist_id=artist_id,
                name=response[TITLE],
                primary_genre=safe_nested_get(response, [GENRES, PRIMARY]),
                label=cls._extract_metadata_item(response, LABEL),
                writers=ShazamWritersExtractor.extract(response)
            )

    @staticmethod
    def _extract_artist_id(response: dict) -> Optional[str]:
        artists = response.get(ARTISTS)

        if artists:
            return artists[0][ADAM_ID]

    @staticmethod
    def _extract_metadata_item(response: dict, title: str) -> str:
        for section in response.get(SECTIONS, []):
            for item in section.get(METADATA, []):
                item_title = item.get(TITLE, '')

                if item_title == title:
                    return item.get(TEXT)
