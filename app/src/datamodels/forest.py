from pydantic import BaseModel, Field


class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., ge=0.0)
    sepal_width: float = Field(..., ge=0.0)
    petal_length: float = Field(..., ge=0.0)
    petal_width: float = Field(..., ge=0.0)


class IrisLabelProbability(BaseModel):
    id: int = Field(..., ge=0)
    probability: float = Field(..., ge=0, le=1.0)
