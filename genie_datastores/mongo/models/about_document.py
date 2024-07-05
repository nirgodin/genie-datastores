from pymongo import TEXT

from genie_datastores.models import DataSource, EntityType
from genie_datastores.mongo.models.base_document import BaseDocument


class AboutDocument(BaseDocument):
    about: str
    entity_type: EntityType
    entity_id: str
    name: str
    source: DataSource

    class Settings:
        name = "abouts"
        indexes = [
            [
                ("about", TEXT),
                ("name", TEXT),
            ],
        ]
