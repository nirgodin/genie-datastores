from sqlalchemy import Column, String, ForeignKey

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID
from genie_datastores.postgres.models import BaseORMModel


class TrackIDMapping(BaseORMModel):
    __tablename__ = "track_ids_mapping"

    id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), primary_key=True, nullable=False)
    adam_id = Column(String)
    apple_music_id = Column(String)
    genius_id = Column(String)
    musixmatch_id = Column(String)
    shazam_id = Column(String)
