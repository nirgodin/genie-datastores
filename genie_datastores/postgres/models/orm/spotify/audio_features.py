from sqlalchemy import Column, String, ForeignKey, SmallInteger, Integer, Boolean, Float

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID
from genie_datastores.postgres.models import BaseORMModel


class AudioFeatures(BaseORMModel):
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
