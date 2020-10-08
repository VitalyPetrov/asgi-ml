import os
from pathlib import Path
from pydantic import validator, BaseSettings, confloat, conint
from dotenv import load_dotenv


PROJECT_ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
load_dotenv()


class MLSettings(BaseSettings):
    num_trees: int = os.getenv("APP_ML_NUM_TREES")
    max_depth: conint(ge=1) = os.getenv("APP_ML_MAX_DEPTH")
    samples_leaf: conint(ge=1) = os.getenv("APP_ML_SAMPLES_ON_LEAF")
    loss_function: str = os.getenv("APP_ML_LOSS_FUNCTION")
    test_size: confloat(lt=1.0) = os.getenv("APP_ML_TEST_SIZE")

    @validator("loss_function", pre=True)
    def is_valid_loss(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError(
                f"loss_function should have str type, got {type(value)} instead"
            )
        if value not in ("gini", "entropy"):
            raise ValueError(
                "Wrong type of loss function. Can be one of ('gini', 'entropy')"
            )
        return value


class Settings(BaseSettings):
    ml: MLSettings = MLSettings()
    api_prefix: str = os.getenv("APP_API_PREFIX")

    @validator("api_prefix", pre=True)
    def is_valid_api_prefix(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError(
                f"API prefix should have str type, got {type(value)} instead"
            )
        return value


settings = Settings()
