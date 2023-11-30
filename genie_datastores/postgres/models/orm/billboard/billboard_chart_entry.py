from sqlalchemy import String, Column, ForeignKey, Integer, Enum, TIMESTAMP, SmallInteger, Boolean, UniqueConstraint

from genie_datastores.postgres.consts.orm_consts import BILLBOARD_TRACK_ID
from genie_datastores.postgres.models.data_classes.chart_entry_data import ChartEntryData
from genie_datastores.postgres.models.enum.billboard_chart import BillboardChart

from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class BillboardChartEntry(BaseORMModel):
    __tablename__ = "billboard_chart_entries"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    billboard_id = Column(String, ForeignKey(BILLBOARD_TRACK_ID), nullable=False)
    chart = Column(Enum(BillboardChart), nullable=False)
    date = Column(TIMESTAMP, nullable=False)
    position = Column(SmallInteger, nullable=False)
    peak_position = Column(SmallInteger)
    last_position = Column(SmallInteger)
    is_new = Column(Boolean)

    UniqueConstraint(billboard_id, chart, date)

    @classmethod
    def from_chart_entry(cls, chart_entry: ChartEntryData) -> "BillboardChartEntry":
        return cls(
            billboard_id=chart_entry.id,
            chart=BillboardChart(chart_entry.chart),
            date=chart_entry.date,
            position=chart_entry.entry.rank,
            peak_position=chart_entry.entry.peakPos,
            last_position=chart_entry.entry.lastPos,
            is_new=chart_entry.entry.isNew
        )
