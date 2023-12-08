from typing import Optional

from genie_common.utils import to_datetime
from sqlalchemy import String, Column, SmallInteger, ForeignKey, Enum, TIMESTAMP

from genie_datastores.postgres.consts.datetime_consts import SPOTIFY_RELEASE_DATE_ORDERED_FORMATS
from genie_datastores.postgres.consts.orm_consts import SPOTIFY_ARTISTS_ID
from genie_datastores.postgres.consts.spotify_consts import ID, NAME, RELEASE_DATE, TOTAL_TRACKS, ALBUM_TYPE
from genie_datastores.postgres.models.enum.spotify_album_type import SpotifyAlbumType
from genie_datastores.postgres.models.orm.spotify.base_spotify_orm_model import BaseSpotifyORMModel
from genie_datastores.postgres.inner_utils.spotify_utils import extract_artist_id


class SpotifyAlbum(BaseSpotifyORMModel):
    __tablename__ = "spotify_albums"

    id = Column(String, primary_key=True, nullable=False)
    artist_id = Column(String, ForeignKey(SPOTIFY_ARTISTS_ID), nullable=False)
    group = Column(Enum(SpotifyAlbumType))
    label = Column(String)  # TODO: Should remove, exists in shazam_tracks
    name = Column(String, nullable=False)
    release_date = Column(TIMESTAMP)
    total_tracks = Column(SmallInteger, nullable=False)
    type = Column(Enum(SpotifyAlbumType))

    @classmethod
    def from_spotify_response(cls, response: dict) -> "SpotifyAlbum":
        album_type = cls._extract_album_type(response)
        return cls(
            id=response[ID],
            artist_id=extract_artist_id(response),
            group=album_type,
            label=None,  # TODO: Rethink
            name=response[NAME],
            release_date=to_datetime(response[RELEASE_DATE], SPOTIFY_RELEASE_DATE_ORDERED_FORMATS),
            total_tracks=response[TOTAL_TRACKS],
            type=album_type
        )

    @staticmethod
    def _extract_album_type(response: dict) -> Optional[SpotifyAlbumType]:
        album_type = response.get(ALBUM_TYPE)
        return None if album_type is None else SpotifyAlbumType(album_type)
