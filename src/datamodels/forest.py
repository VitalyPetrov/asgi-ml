from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator


class IrisLabelProbability(BaseModel):
    id: int = Field(..., ge=0)
    probability: float = Field(..., ge=0, le=1.0)


class IrisClassificationResponse(BaseModel):
    label_probability: IrisLabelProbability
    create_dtm: Optional[datetime] = None

    @validator("create_dtm", always=True)
    def set_create_dtm(cls, value: datetime) -> datetime:
        return value or datetime.now()


class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., ge=0.0)
    sepal_width: float = Field(..., ge=0.0)
    petal_length: float = Field(..., ge=0.0)
    petal_width: float = Field(..., ge=0.0)

    @classmethod
    def get_2d_representation(cls, features):
        return [list(features.dict().values())]
