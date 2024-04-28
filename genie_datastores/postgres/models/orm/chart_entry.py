from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, SmallInteger, UniqueConstraint, Enum, \
    CheckConstraint, JSON

from genie_datastores.postgres.consts.orm_consts import SPOTIFY_TRACKS_ID
from genie_datastores.postgres.models.enum.chart import Chart
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class ChartEntry(BaseORMModel):
    __tablename__ = "charts_entries"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    chart = Column(Enum(Chart), nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    position = Column(SmallInteger, nullable=False)
    comment = Column(String)
    entry_metadata = Column(JSON)
    key = Column(String)
    track_id = Column(String, ForeignKey(SPOTIFY_TRACKS_ID))

    UniqueConstraint(track_id, chart, date)
    UniqueConstraint(key, chart, date)
    CheckConstraint("key is not null or track_id is not null", name="check_track_id_and_key_are_not_both_null")
