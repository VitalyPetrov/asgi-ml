import enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class HealthStatus(str, enum.Enum):
    status_pass = "pass"
    status_fail = "fail"
    status_warn = "warn"


class Health(BaseModel):
    status: HealthStatus = HealthStatus.status_pass
    version: Optional[str] = None
    release_id: Optional[str] = None
    description: Optional[str] = None

    class Config:
        validate_assignment = True
        json_encoders = {
            datetime: lambda x: (
                x.isoformat(timespec="milliseconds").replace("+00:00", "Z")
            )
        }
