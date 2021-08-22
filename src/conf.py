import os
from datetime import timedelta

from pydantic import BaseSettings, confloat, conint, validator


class RedisSettings(BaseSettings):
    host: str = ""
    port: int = 6379
    db: int = 0

    class Config:
        env_prefix = "APP_REDIS_"


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
                "loss_function should have str type"
                f"got {type(value)} instead"
            )
        if value not in ("gini", "entropy"):
            raise ValueError(
                "Wrong type of loss function."
                "Can be one of ('gini', 'entropy')"
            )
        return value


class Settings(BaseSettings):
    redis: RedisSettings = RedisSettings()
    ml: MLSettings = MLSettings()
    cache_ttl: int = int(timedelta(days=7).total_seconds())
    api_prefix: str = os.getenv("APP_API_PREFIX")

    @validator("api_prefix", pre=True)
    def is_valid_api_prefix(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError(
                f"API prefix should have str type, got {type(value)} instead"
            )
        return value


settings = Settings()
