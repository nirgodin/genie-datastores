import os
from functools import lru_cache
from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient


@lru_cache
def get_mongo_uri() -> str:
    return os.environ["MONGO_URI"]


@lru_cache
def get_motor_client(uri: Optional[str] = None) -> AsyncIOMotorClient:
    mongo_uri = uri or get_mongo_uri()
    return AsyncIOMotorClient(mongo_uri)
