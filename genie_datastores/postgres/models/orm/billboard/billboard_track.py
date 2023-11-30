from typing import Optional

from genie_common.utils import safe_nested_get
from sqlalchemy import Column, String, SmallInteger

from genie_datastores.postgres.consts.orm_consts import BILLBOARD_TRACKS_TABLE
from genie_datastores.postgres.consts.spotify_consts import TRACK, ID
from genie_datastores.postgres.models.data_classes.chart_entry_data import ChartEntryData
from genie_datastores.postgres.models.orm.base_orm_model import BaseORMModel


class BillboardTrack(BaseORMModel):
    __tablename__ = BILLBOARD_TRACKS_TABLE

    id = Column(String, primary_key=True, nullable=False)
    track_id = Column(String)
    weeks_on_chart = Column(SmallInteger)

    @classmethod
    def from_chart_entry(cls, chart_entry: ChartEntryData) -> "BillboardTrack":
        return cls(
            id=chart_entry.id,
            track_id=cls._extract_track_id(chart_entry),
            weeks_on_chart=chart_entry.entry.weeks
        )

    @staticmethod
    def _extract_track_id(chart_entry: ChartEntryData) -> Optional[str]:
        if chart_entry.track is not None:
            return safe_nested_get(chart_entry.track, [TRACK, ID])
