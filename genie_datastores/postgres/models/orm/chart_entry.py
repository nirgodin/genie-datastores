from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, SmallInteger, UniqueConstraint, Enum

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID
from genie_datastores.postgres.models.enum.chart import Chart
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class ChartEntry(BaseORMModel):
    __tablename__ = "charts_entries"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    track_id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID), nullable=False)
    chart = Column(Enum(Chart), nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    key = Column(String, nullable=False)
    position = Column(SmallInteger, nullable=False)
    comment = Column(String)

    UniqueConstraint(track_id, chart, date)
