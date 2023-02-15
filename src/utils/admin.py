import re

from fastapi import Request

SLUG_RE = re.compile(r"\W")


def get_version(request: Request):
    return request.app.version


def get_slug(request: Request):
    return SLUG_RE.sub("-", request.app.title.lower())
