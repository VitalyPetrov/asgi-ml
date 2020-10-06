from fastapi import APIRouter, Depends
from starlette.responses import Response
from starlette_prometheus import metrics

from ..datamodels.monitor import Health, HealthStatus
from ..utils.admin import get_slug, get_version


def health_check(
    slug: str = Depends(get_slug), version: str = Depends(get_version)
):
    health = Health(
        status=HealthStatus.status_pass,
        version=version.split(".", 1)[0],
        release_id=version,
        description=slug
    )
    return Response(
        content=health.json(by_alias=True, skip_defaults=True),
        media_type="application/health+jsom",
    )


router = APIRouter()
router.add_api_route("/metrics", metrics)
router.add_api_route("/health", health_check, response_model=Health)
