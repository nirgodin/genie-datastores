from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID, SPOTIFY_ARTISTS_ID
from genie_datastores.postgres.models import BaseORMModel


class SpotifyFeaturedArtist(BaseORMModel):
    __tablename__ = 'spotify_featured_artists'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    track_id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), nullable=False)
    artist_id = Column(String, ForeignKey(SPOTIFY_ARTISTS_ID), nullable=False)
    position = Column(Integer, nullable=False)

    UniqueConstraint(track_id, artist_id)
