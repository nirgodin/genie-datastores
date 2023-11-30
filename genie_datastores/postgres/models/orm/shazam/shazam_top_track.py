from sqlalchemy import Column, String, Enum, SmallInteger, Integer, UniqueConstraint, TIMESTAMP

from genie_datastores.postgres.models.enum.shazam_location import ShazamLocation
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class ShazamTopTrack(BaseORMModel):
    __tablename__ = "shazam_top_tracks"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    date = Column(TIMESTAMP, nullable=False)
    location = Column(Enum(ShazamLocation), nullable=False)
    position = Column(SmallInteger, nullable=False)
    track_id = Column(String)  # TODO: Add ForeignKey to shazam_tracks

    UniqueConstraint(date, location, position)
