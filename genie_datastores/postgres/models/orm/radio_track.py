from datetime import datetime

from genie_common.utils import safe_nested_get
from sqlalchemy import Column, Integer, SmallInteger, String, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy import Enum

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID
from genie_datastores.postgres.consts.spotify_consts import TRACK, ID, ADDED_AT, SNAPSHOT_ID, POPULARITY, FOLLOWERS, \
    TOTAL, SPOTIFY_DATETIME_FORMAT
from genie_datastores.postgres.models.enum.spotify_station import SpotifyStation
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class RadioTrack(BaseORMModel):
    __tablename__ = "radio_tracks"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    track_id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), nullable=False)
    added_at = Column(TIMESTAMP, nullable=False)
    artist_followers = Column(Integer, nullable=False)
    artist_popularity = Column(SmallInteger, nullable=False)
    popularity = Column(SmallInteger, nullable=False)
    snapshot_id = Column(String, nullable=False)
    station = Column(Enum(SpotifyStation), nullable=False)

    UniqueConstraint(track_id, added_at, station)

    @classmethod
    def from_playlist_artist_track(cls, playlist: dict, artist: dict, track: dict) -> "RadioTrack":
        return cls(
            track_id=safe_nested_get(track, [TRACK, ID]),
            added_at=datetime.strptime(track[ADDED_AT], SPOTIFY_DATETIME_FORMAT),
            artist_followers=safe_nested_get(artist, [FOLLOWERS, TOTAL]),
            artist_popularity=artist[POPULARITY],
            popularity=safe_nested_get(track, [TRACK, POPULARITY]),
            snapshot_id=playlist[SNAPSHOT_ID],
            station=SpotifyStation(playlist[ID]),
        )
