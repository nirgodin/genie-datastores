from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY

from genie_datastores.postgres.consts.orm_consts import SHAZAM_TRACKS_TABLE, SHAZAM_ARTIST_ID
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class ShazamTrack(BaseORMModel):
    __tablename__ = SHAZAM_TRACKS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    artist_id = Column(String, ForeignKey(SHAZAM_ARTIST_ID), nullable=False)
    name = Column(String, nullable=False)
    label = Column(String)
    writers = Column(ARRAY(String))
    primary_genre = Column(String)
