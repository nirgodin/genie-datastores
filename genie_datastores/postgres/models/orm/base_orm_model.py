from datetime import datetime
from typing import Any, Dict

from sqlalchemy import TIMESTAMP, Column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseORMModel(Base):
    __abstract__ = True

    creation_date = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    update_date = Column(TIMESTAMP, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in vars(self).items() if not k.startswith("_")}
