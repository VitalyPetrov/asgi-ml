from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette_prometheus import metrics

from src.datamodels.monitor import Health, HealthStatus
from src.dependencies.base import get_slug, get_version


def health_check(
    slug: str = Depends(get_slug), version: str = Depends(get_version)
) -> Response:
    health = Health(
        status=HealthStatus.status_pass,
        version=version.split(".", 1)[0],
        release_id=version,
        description=slug,
    )
    return Response(
        content=health.json(by_alias=True, exclude_unset=True),
        media_type="application/health+json",
    )


router = APIRouter()
router.add_api_route("/metrics", metrics)
router.add_api_route("/health", health_check, response_model=Health)
