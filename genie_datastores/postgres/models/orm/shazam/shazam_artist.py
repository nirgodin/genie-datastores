from sqlalchemy import String, Column, TIMESTAMP, Boolean
from sqlalchemy.dialects.postgresql import ARRAY

from genie_datastores.postgres.consts.orm_consts import SHAZAM_ARTISTS_TABLE
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class ShazamArtist(BaseORMModel):
    __tablename__ = SHAZAM_ARTISTS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    has_about_document = Column(Boolean, nullable=False, default=False)
    birth_date = Column(TIMESTAMP)
    genres = Column(ARRAY(String))
    origin = Column(String)
    similar_artists = Column(ARRAY(String))
