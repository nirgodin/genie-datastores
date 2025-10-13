from sqlalchemy import Column, String, ForeignKey, SmallInteger, Boolean, TIMESTAMP

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_TABLE, SPOTIFY_ARTISTS_ID
from genie_datastores.postgres.models import BaseORMModel


class SpotifyTrack(BaseORMModel):
    __tablename__ = SPOTIFY_TRACKS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    album_id = Column(String)  # ForeignKey("spotify_albums.id"), nullable=False  # TODO: Add back after albums collection
    artist_id = Column(String, ForeignKey(SPOTIFY_ARTISTS_ID), nullable=False)
    explicit = Column(Boolean, nullable=False)
    name = Column(String, nullable=False)
    number = Column(SmallInteger, nullable=False)
    release_date = Column(TIMESTAMP)
