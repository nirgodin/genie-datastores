from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_ARTISTS_TABLE
from genie_datastores.postgres.models import BaseORMModel


class SpotifyArtist(BaseORMModel):
    __tablename__ = SPOTIFY_ARTISTS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    has_about_document = Column(Boolean, nullable=False, default=False)
    facebook_name = Column(String)
    genres = Column(ARRAY(String))
    instagram_name = Column(String)
    twitter_name = Column(String)
    wikipedia_language = Column(String)
    wikipedia_name = Column(String)
