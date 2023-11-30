from sqlalchemy import Column, String, ForeignKey, ARRAY, SmallInteger, JSON, Enum

from postgres_client.consts.orm_consts import SPOTIFY_TRACKS_ID
from postgres_client.models.enum.data_source import DataSource
from postgres_client.models.orm.base_orm_model import BaseORMModel


class TrackLyrics(BaseORMModel):
    __tablename__ = "tracks_lyrics"

    id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), primary_key=True, nullable=False)
    lyrics = Column(ARRAY(String))
    lyrics_source = Column(Enum(DataSource))
    language = Column(String)
    language_confidence = Column(SmallInteger)
    number_of_words = Column(SmallInteger)
    words_count = Column(JSON)
