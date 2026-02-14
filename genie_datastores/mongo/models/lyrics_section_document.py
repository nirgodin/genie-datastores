from typing import List

from genie_datastores.models import DataSource
from genie_datastores.mongo.models import BaseDocument
from genie_datastores.mongo.models.lyrics_section_type import LyricsSectionType


class LyricsSectionDocument(BaseDocument):
    entity_id: str
    number: int
    lines: List[str]
    source: DataSource
    type: LyricsSectionType
