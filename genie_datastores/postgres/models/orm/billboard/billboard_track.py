from typing import Optional

from sqlalchemy import Column, String, SmallInteger

from postgres_client import BaseORMModel
from postgres_client.consts.orm_consts import BILLBOARD_TRACKS_TABLE
from postgres_client.consts.spotify_consts import ID, TRACK
from postgres_client.models.data_classes.chart_entry_data import ChartEntryData
from postgres_client.utils.dict_utils import safe_nested_get


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
