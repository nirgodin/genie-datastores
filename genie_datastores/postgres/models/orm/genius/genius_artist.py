from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import ARRAY

from genie_datastores.postgres.models import BaseORMModel


class GeniusArtist(BaseORMModel):
    __tablename__ = "genius_artists"

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    alternate_names = Column(ARRAY(String))
    facebook_name = Column(String)
    instagram_name = Column(String)
    twitter_name = Column(String)
