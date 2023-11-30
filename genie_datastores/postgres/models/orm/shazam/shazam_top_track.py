from sqlalchemy import Column, String, Enum, SmallInteger, Integer, ForeignKey, UniqueConstraint, TIMESTAMP

from postgres_client import BaseORMModel
from postgres_client.consts.orm_consts import SHAZAM_TRACK_ID
from postgres_client.models.enum.shazam_location import ShazamLocation


class ShazamTopTrack(BaseORMModel):
    __tablename__ = "shazam_top_tracks"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    date = Column(TIMESTAMP, nullable=False)
    location = Column(Enum(ShazamLocation), nullable=False)
    position = Column(SmallInteger, nullable=False)
    track_id = Column(String)

    UniqueConstraint(date, location, position)
