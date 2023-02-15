import os
import sys
import logging
from datetime import timedelta
from typing import Literal

from pydantic import BaseSettings, confloat, conint


class RedisSettings(BaseSettings):
    host: str = ""
    port: int = 6379
    db: int = 0

    class Config:
        env_prefix = "APP_REDIS_"


class MLSettings(BaseSettings):
    num_trees: int
    max_depth: conint(ge=1)
    samples_on_leaf: conint(ge=1) = os.getenv("APP_ML_SAMPLES_ON_LEAF")
    loss_function: Literal["gini", "entropy"]
    test_size: confloat(gt=0.0, lt=1.0)

    class Config:
        env_prefix = "APP_ML_"


class Settings(BaseSettings):
    redis: RedisSettings = RedisSettings()
    # ml: MLSettings = MLSettings()
    cache_ttl: int = int(timedelta(days=7).total_seconds())
    api_prefix: str = os.getenv("APP_API_PREFIX")


settings = Settings()

# configure logger object
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s | [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
