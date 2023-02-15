import asyncio

from fastapi import FastAPI

from src.conf import settings
from src.dependency import ml
from src.routers import forest, monitor

__version__ = "1.0.0"


app = FastAPI(
    title="Simple ASGI ML SVC",
    openapi_prefix=settings.api_prefix,
    version=__version__,
)


# Setup monitor and ml routes
app.include_router(
    monitor.router, prefix="", responses={404: {"description": "Not found"}}
)
app.include_router(
    forest.router,
    prefix="/classification",
    responses={404: {"description": "Not found"}},
)


@app.on_event("startup")
async def startup():
    app.state.settings = settings

    try:
        coroutine = ml.on_startup(app)
        if asyncio.iscoroutine(coroutine):
            await coroutine
    except Exception as e:
        try:
            await shutdown()
        finally:
            raise e


@app.on_event("shutdown")
async def shutdown():
    try:
        coroutine = ml.on_shutdown(app)
        if asyncio.iscoroutine(coroutine):
            await coroutine
    except Exception as e:
        raise e
