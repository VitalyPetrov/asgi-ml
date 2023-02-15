from typing import List

from fastapi import APIRouter, Depends

from src.datamodels.forest import IrisClassificationResponse, IrisFeatures
from src.dependency.ml import ML, get_ml

router = APIRouter()


@router.post("/classify-iris", response_model=List[IrisClassificationResponse])
async def classify_iris(
    sepal_length: float,
    sepal_width: float,
    petal_length: float,
    petal_width: float,
    ml: ML = Depends(get_ml),
) -> List[IrisClassificationResponse]:
    features = IrisFeatures(
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width,
    )
    return await ml.classify(features=features)
