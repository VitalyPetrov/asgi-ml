from fastapi import FastAPI
from .conf import settings


__version__ = "0.1.0"


app = FastAPI(
    title="Simple ASGI ML service",
    openapi_prefix=settings.api_prefix,
    version=__version__,
)

# TODO: add routers and include them to the app
