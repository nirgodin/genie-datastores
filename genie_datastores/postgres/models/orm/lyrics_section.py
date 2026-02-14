from sqlalchemy import Column, String

from genie_datastores.postgres.models import BaseORMModel


class LyricsSection(BaseORMModel):
    __tablename__ = "lyrics_sections"

    id = Column(String, primary_key=True, nullable=False)
    track_id = Column(String, nullable=False)
