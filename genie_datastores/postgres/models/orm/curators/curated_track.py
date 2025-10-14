from sqlalchemy import Column, String, ForeignKey, Integer, TIMESTAMP, UniqueConstraint

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID, CURATORS_COLLECTIONS_TABLE_ID
from genie_datastores.postgres.models import BaseORMModel


class CuratedTrack(BaseORMModel):
    __tablename__ = "curated_tracks"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    track_id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    collection = Column(String, ForeignKey(CURATORS_COLLECTIONS_TABLE_ID), nullable=False)

    UniqueConstraint(track_id, collection)
