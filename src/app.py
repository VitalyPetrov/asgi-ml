from fastapi import FastAPI
from .conf import settings

from .routers import monitor


__version__ = "0.1.0"


app = FastAPI(
    title="Simple ASGI ML SVC",
    openapi_prefix=settings.api_prefix,
    version=__version__,
)


# Setup monitor and ml routes
app.include_router(
    monitor.router, prefix="", responses={404: {"description": "Not found"}}
)
# TODO: add some basic ML routes
#
