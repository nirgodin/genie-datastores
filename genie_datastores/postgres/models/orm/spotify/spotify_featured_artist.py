from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID, SPOTIFY_ARTISTS_ID
from genie_datastores.postgres.consts.spotify_consts import ID
from genie_datastores.postgres.models.orm.spotify.base_spotify_orm_model import BaseSpotifyORMModel


class SpotifyFeaturedArtist(BaseSpotifyORMModel):
    __tablename__ = 'spotify_featured_artists'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    track_id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), nullable=False)
    artist_id = Column(String, ForeignKey(SPOTIFY_ARTISTS_ID), nullable=False)
    position = Column(Integer, nullable=False)

    UniqueConstraint(track_id, artist_id)

    @classmethod
    def from_spotify_response(cls, response: dict) -> "SpotifyFeaturedArtist":
        return cls(
            track_id=response[ID],
            artist_id=response["artist_id"],
            position=response["position"],
        )
