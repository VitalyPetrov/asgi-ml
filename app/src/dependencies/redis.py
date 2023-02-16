from fastapi import FastAPI, Request
from redis.asyncio import Redis as AsyncRedis

from src.conf import logger


__all__ = ("get_redis",)


async def get_redis(request: Request):
    return request.app.state.redis


async def on_startup(app: FastAPI) -> None:
    logger.info("Redis dependency: start")
    app.state.redis: AsyncRedis = AsyncRedis.from_url(
        app.state.settings.redis.dsn
    )
    await app.state.redis.ping()


async def on_shutdown(app: FastAPI) -> None:
    logger.info("Redis dependency: shutdown")
    await app.state.redis.close()
