import re
from fastapi import FastAPI, Request

__all__ = (
    "get_slug",
    "get_version",
)

SLUG_RE = re.compile(r"\W")


def get_version(request: Request):
    return request.app.version


def get_slug(request: Request):
    return SLUG_RE.sub("-", request.app.title.lower())


async def on_startup(app: FastAPI):
    pass


async def on_shutdown(app: FastAPI):
    pass
