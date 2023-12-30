from functools import lru_cache

from aioredis import Redis


@lru_cache
def get_redis() -> Redis:
    return Redis()
