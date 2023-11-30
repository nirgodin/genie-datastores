from sqlalchemy import Column, String, ForeignKey

from postgres_client import BaseSpotifyORMModel
from postgres_client.consts.orm_consts import SPOTIFY_TRACKS_ID
from postgres_client.consts.spotify_consts import ID, TRACK
from postgres_client.utils.dict_utils import safe_nested_get


class TrackIDMapping(BaseSpotifyORMModel):
    __tablename__ = "track_ids_mapping"

    id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), primary_key=True, nullable=False)
    adam_id = Column(String)
    apple_music_id = Column(String)
    genius_id = Column(String)
    musixmatch_id = Column(String)
    shazam_id = Column(String)

    @classmethod
    def from_spotify_response(cls, response: dict) -> "TrackIDMapping":
        return cls(
            id=safe_nested_get(response, [TRACK, ID])
        )
