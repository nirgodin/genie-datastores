from datetime import timedelta
from functools import wraps
from typing import Optional

from aioredis import Redis
from genie_common.encoders import IEncoder
from genie_common.tools import logger
from genie_common.typing import AF
from genie_common.utils import is_primitive, sort_dict_by_key

from genie_datastores.redis.operations import get_redis


class RedisClient:
    @staticmethod
    def cache(encoder: IEncoder, ttl: timedelta):
        def decorator(func: AF):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                redis = get_redis()
                cache_key = RedisClient._build_cache_key(*args, **kwargs)
                result = await RedisClient._retrieve_from_cache(redis, cache_key, encoder)

                if result is None:
                    result = await RedisClient._execute_and_set_cache(
                        redis=redis,
                        cache_key=cache_key,
                        ttl=ttl,
                        encoder=encoder,
                        func=func,
                        *args,
                        **kwargs
                    )

                return result

            return wrapper

        return decorator

    @staticmethod
    def _build_cache_key(*args, **kwargs) -> str:
        sorted_kwargs = sort_dict_by_key(kwargs, reverse=False)
        function_args = list(args) + list(sorted_kwargs.values())
        key_components = []

        for arg in function_args:
            if is_primitive(arg):
                key_components.append(str(arg))

        return "_".join(key_components)

    @staticmethod
    async def _retrieve_from_cache(redis: Redis, cache_key: str, encoder: IEncoder) -> Optional[dict]:
        cached_result = await redis.get(cache_key)

        if cached_result is None:
            logger.info(f"Did not find result in cache for cache key `{cache_key}`. Sending fetch request.")

        else:
            logger.info(f"Found result in cache for cache key `{cache_key}`.")
            return encoder.decode(cached_result)

    @staticmethod
    async def _execute_and_set_cache(redis: Redis,
                                     cache_key: str,
                                     ttl: timedelta,
                                     encoder: IEncoder,
                                     func: AF,
                                     *args,
                                     **kwargs) -> dict:
        result = await func(*args, **kwargs)
        encoded_result = encoder.encode(result)
        await redis.setex(name=cache_key, time=ttl, value=encoded_result)
        logger.info(f"Successfully set cache for cache key `{cache_key}`.")

        return result
