from typing import Optional, Any

from genie_common.tools import logger
from sqlalchemy import Column, String, ForeignKey, SmallInteger, Integer, Boolean, Float

from genie_datastores.postgres.consts.audio_features_consts import ACOUSTICNESS, DANCEABILITY, DURATION_MS, ENERGY, \
    INSTRUMENTALNESS, KEY, LIVENESS, LOUDNESS, MODE, SPEECHINESS, TEMPO, TIME_SIGNATURE, VALENCE
from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID
from genie_datastores.postgres.consts.spotify_consts import ID
from genie_datastores.postgres.models.orm.spotify.base_spotify_orm_model import BaseSpotifyORMModel


class AudioFeatures(BaseSpotifyORMModel):
    __tablename__ = "audio_features"

    id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), primary_key=True, nullable=False)
    acousticness = Column(SmallInteger)
    danceability = Column(SmallInteger)
    duration_ms = Column(Integer)
    energy = Column(SmallInteger)
    instrumentalness = Column(SmallInteger)
    key = Column(SmallInteger)
    liveness = Column(SmallInteger)
    loudness = Column(Float)
    mode = Column(Boolean)
    speechiness = Column(SmallInteger)
    tempo = Column(SmallInteger)
    time_signature = Column(SmallInteger)
    valence = Column(SmallInteger)

    @classmethod
    def from_spotify_response(cls, response: dict) -> Optional["AudioFeatures"]:
        if not cls._is_valid_response(response):
            logger.warning("Received invalid audio features response from Spotify. Returning None")
            return None

        return cls(
            id=response[ID],
            acousticness=cls._safe_multiply_round(response[ACOUSTICNESS]),
            danceability=cls._safe_multiply_round(response[DANCEABILITY]),
            duration_ms=response[DURATION_MS],
            energy=cls._safe_multiply_round(response[ENERGY]),
            instrumentalness=cls._safe_multiply_round(response[INSTRUMENTALNESS]),
            key=response[KEY],
            liveness=cls._safe_multiply_round(response[LIVENESS]),
            loudness=response[LOUDNESS],
            mode=response[MODE],
            speechiness=cls._safe_multiply_round(response[SPEECHINESS]),
            tempo=cls._safe_round(response[TEMPO]),
            time_signature=response[TIME_SIGNATURE],
            valence=cls._safe_multiply_round(response[VALENCE])
        )

    @staticmethod
    def _is_valid_response(response: Any) -> bool:
        if isinstance(response, dict):
            return ID in response.keys()

        return False

    @staticmethod
    def _safe_multiply_round(value: Optional[float]) -> Optional[int]:
        if value is not None:
            return round(value * 100)

    @staticmethod
    def _safe_round(value: Optional[float]) -> Optional[int]:
        if value is not None:
            return round(value)
