from sqlalchemy import Column, String, Enum

from genie_datastores.postgres.models import BaseORMModel, DataSource, EntityType


class Translation(BaseORMModel):
    __tablename__ = "translations"

    id = Column(String, primary_key=True, nullable=False)
    entity_source = Column(Enum(DataSource), nullable=False)
    entity_type = Column(Enum(EntityType), nullable=False)
    text = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    source_language = Column(String, nullable=False)
    target_language = Column(String, nullable=False)
