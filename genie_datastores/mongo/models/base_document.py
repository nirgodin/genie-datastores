from datetime import datetime

from beanie import Document
from pydantic import Field


class BaseDocument(Document):
    creation_date: datetime = Field(default_factory=datetime.utcnow)
    update_date: datetime = Field(default_factory=datetime.utcnow)
