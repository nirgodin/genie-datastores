from sqlalchemy import String, Column, ForeignKey, Enum, Boolean

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID
from genie_datastores.postgres.models import BaseORMModel, PrimaryGenre


class Track(BaseORMModel):
    __tablename__ = "tracks"

    id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), primary_key=True, nullable=False)
    primary_genre = Column(Enum(PrimaryGenre))
    is_cover = Column(Boolean, default=False)
