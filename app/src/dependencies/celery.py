from fastapi import FastAPI, Request
from celery import Celery

from src.conf import logger


__all__ = ("get_celery",)


async def get_celery(request: Request):
    return request.app.state.celery


async def on_startup(app: FastAPI) -> None:
    logger.info("Celery dependency: start")
    app.state.celery: Celery = Celery(
        "tasks",
        broker=app.state.settings.rabbitmq.uri,
        backend=app.state.settings.redis.dsn,
    )


async def on_shutdown(app: FastAPI) -> None:
    logger.info("Celery dependency: shutdown")
    app.state.celery.close()
