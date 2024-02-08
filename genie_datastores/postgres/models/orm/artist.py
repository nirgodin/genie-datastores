from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, Boolean, Float, Enum

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_ARTISTS_ID, SHAZAM_ARTIST_ID
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel
from genie_datastores.postgres.models.enum.gender import Gender
from genie_datastores.postgres.models.enum.data_source import DataSource


class Artist(BaseORMModel):
    __tablename__ = "artists"

    id = Column(String, ForeignKey(SPOTIFY_ARTISTS_ID), primary_key=True, nullable=False)
    shazam_id = Column(String, ForeignKey(SHAZAM_ARTIST_ID))
    birth_date = Column(TIMESTAMP)
    death_date = Column(TIMESTAMP)
    birth_date_source = Column(Enum(DataSource))
    gender = Column(Enum(Gender))
    gender_source = Column(Enum(DataSource))
    is_israeli = Column(Boolean)
    is_lgbtq = Column(Boolean)
    primary_genre = Column(String)  # TODO: Consider making enum
    country = Column(String)
    state = Column(String)
    county = Column(String)
    city = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    @classmethod
    def from_id(cls, id_: str) -> "Artist":
        return cls(id=id_)
