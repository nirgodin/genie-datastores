from sqlalchemy import String, Column, SmallInteger, ForeignKey, Enum, TIMESTAMP

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_ARTISTS_ID
from genie_datastores.postgres.models import BaseORMModel
from genie_datastores.postgres.models.enum.spotify_album_type import SpotifyAlbumType


class SpotifyAlbum(BaseORMModel):
    __tablename__ = "spotify_albums"

    id = Column(String, primary_key=True, nullable=False)
    artist_id = Column(String, ForeignKey(SPOTIFY_ARTISTS_ID), nullable=False)
    group = Column(Enum(SpotifyAlbumType))
    label = Column(String)  # TODO: Should remove, exists in shazam_tracks
    name = Column(String, nullable=False)
    release_date = Column(TIMESTAMP)
    total_tracks = Column(SmallInteger, nullable=False)
    type = Column(Enum(SpotifyAlbumType))
