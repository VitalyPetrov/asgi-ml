from datetime import datetime
from pydantic import BaseModel, Field, validator


class IrisTypeProbability(BaseModel):
    id: int = Field(..., ge=0)
    probability: float = Field(..., ge=0, lt=1.0)


class IrisClassificationResponse(BaseModel):
    type_probability: IrisTypeProbability
    create_dtm: datetime

    @validator("create_dtm", always=True)
    def set_create_dtm(cls, value: datetime) -> datetime:
        return value or datetime.now()
