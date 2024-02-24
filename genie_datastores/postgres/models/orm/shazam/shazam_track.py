from typing import Optional

from genie_common.utils import safe_nested_get
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY

from genie_datastores.postgres.consts.audio_features_consts import KEY
from genie_datastores.postgres.consts.orm_consts import SHAZAM_TRACKS_TABLE, SHAZAM_ARTIST_ID
from genie_datastores.postgres.consts.shazam_consts import TITLE, PRIMARY, LABEL, ADAM_ID, SECTIONS, METADATA, TEXT
from genie_datastores.postgres.consts.spotify_consts import GENRES
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel
from genie_datastores.postgres.tools.shazam_writers_extractor import ShazamWritersExtractor
from genie_datastores.postgres.inner_utils.spotify_utils import extract_artist_id


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
        artist_id = extract_artist_id(response, ADAM_ID)
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
    def _extract_metadata_item(response: dict, title: str) -> str:
        for section in response.get(SECTIONS, []):
            for item in section.get(METADATA, []):
                item_title = item.get(TITLE, '')

                if item_title == title:
                    return item.get(TEXT)
