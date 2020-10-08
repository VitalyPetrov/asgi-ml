from fastapi import APIRouter, Depends
from typing import List

from ..datamodels.forest import IrisTypeProbability, IrisClassificationResponse
from ..dependency.ml import ML, get_ml

router = APIRouter()

@router.post(
    "/classigy-iris", response_model=List[IrisClassificationResponse]
)
async def classify_iris(
    sepal_length: float,
    sepal_width: float,
    petal_length: float,
    petal_width: float,
    ml: ML = Depends(get_ml)
) -> List[IrisClassificationResponse]:
