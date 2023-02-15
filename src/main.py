import asyncio

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette_prometheus import PrometheusMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException


from src.conf import settings, logger
from src.dependencies import base, redis
from src.routers import monitor


__version__ = "1.0.0"


def setup_app(application: FastAPI) -> None:
    dependencies = [base, redis]

    @application.on_event("startup")
    async def startup():
        application.state.settings = settings

        try:
            for dependency in dependencies:
                coro = dependency.on_startup(application)
                if asyncio.iscoroutine(coro):
                    await coro
        except Exception as e:
            try:
                await shutdown()
            finally:
                raise e

    @application.on_event("shutdown")
    async def shutdown():
        for dependency in reversed(dependencies):
            try:
                coro = dependency.on_shutdown(application)
                if asyncio.iscoroutine(coro):
                    await coro
            except Exception as e:
                raise e


app = FastAPI(
    title="ASGI ML SVC",
    description="Simple API to submit and schedule jobs for remote ML models",
    openapi_prefix=settings.api_prefix,
    version=__version__,
)


setup_app(app)
app.add_middleware(PrometheusMiddleware)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(
    request: Request, exc: StarletteHTTPException
) -> JSONResponse:
    query_params = request.path_params | dict(request.query_params)
    params = ",".join([f"{k}={v}" for k, v in query_params.items()])
    logger.error(f"[{params}] Error: {exc.detail}")

    return JSONResponse(
        status_code=exc.status_code, content={"detail": exc.detail}
    )


# Setup monitor routers
app.include_router(
    monitor.router,
    tags=["monitoring"],
    responses={404: {"description": "Not found"}},
)
