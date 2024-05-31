from sqlalchemy import Column, String, Enum, Integer

from genie_datastores.postgres.models import BaseORMModel, DataSource, EntityType


class Translation(BaseORMModel):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    text = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    source_language = Column(String, nullable=False)
    target_language = Column(String, nullable=False)
    entity_id = Column(String, nullable=True)
    entity_source = Column(Enum(DataSource), nullable=True)
    entity_type = Column(Enum(EntityType), nullable=True)
