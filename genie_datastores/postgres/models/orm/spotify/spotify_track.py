from datetime import datetime
from typing import Optional

from genie_common.utils import safe_nested_get, to_datetime
from sqlalchemy import Column, String, ForeignKey, SmallInteger, Boolean, TIMESTAMP

from genie_datastores.postgres.consts.datetime_consts import SPOTIFY_RELEASE_DATE_ORDERED_FORMATS
from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_TABLE, SPOTIFY_ARTISTS_ID
from genie_datastores.postgres.consts.spotify_consts import TRACK, ID, ALBUM, EXPLICIT, NAME, TRACK_NUMBER, RELEASE_DATE
from genie_datastores.postgres.inner_utils.spotify_utils import extract_artist_id
from genie_datastores.postgres.models.orm.spotify.base_spotify_orm_model import BaseSpotifyORMModel


class SpotifyTrack(BaseSpotifyORMModel):
    __tablename__ = SPOTIFY_TRACKS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    album_id = Column(String)  # ForeignKey("spotify_albums.id"), nullable=False  # TODO: Add back after albums collection
    artist_id = Column(String, ForeignKey(SPOTIFY_ARTISTS_ID), nullable=False)
    explicit = Column(Boolean, nullable=False)
    name = Column(String, nullable=False)
    number = Column(SmallInteger, nullable=False)
    release_date = Column(TIMESTAMP)

    @classmethod
    def from_spotify_response(cls, response: dict) -> "SpotifyTrack":
        inner_track = response[TRACK]
        return cls(
            id=inner_track[ID],
            artist_id=extract_artist_id(inner_track),
            album_id=safe_nested_get(inner_track, [ALBUM, ID], default=None),
            explicit=inner_track.get(EXPLICIT, False),
            name=inner_track[NAME],
            number=inner_track[TRACK_NUMBER],
            release_date=cls._extract_release_date(inner_track),
        )

    @staticmethod
    def _extract_release_date(inner_track: dict) -> Optional[datetime]:
        release_date = safe_nested_get(inner_track, [ALBUM, RELEASE_DATE])
        return to_datetime(release_date, SPOTIFY_RELEASE_DATE_ORDERED_FORMATS)
