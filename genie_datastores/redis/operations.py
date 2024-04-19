import os
from functools import lru_cache

from redis import Redis
from typing import Optional


@lru_cache
def get_redis(host: Optional[str] = None,
              port: Optional[str] = None,
              username: Optional[str] = None,
              password: Optional[str] = None,
              db: Optional[str] = None) -> Redis:

    return Redis(
        host=host or os.environ["REDIS_HOST"],
        port=port or int(os.environ["REDIS_PORT"]),
        username=username or os.environ["REDIS_USERNAME"],
        password=password or os.environ["REDIS_PASSWORD"],
        db=db or int(os.getenv("REDIS_DB", 0))
    )
