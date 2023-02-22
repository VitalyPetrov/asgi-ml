import sys
import logging
from typing import Literal

from pydantic import (
    BaseSettings,
    confloat,
    conint,
    AnyUrl,
    root_validator,
    Field,
)


class RedisSettings(BaseSettings):
    host: str
    port: int
    db: conint(ge=0)
    dsn: AnyUrl = None

    @root_validator(skip_on_failure=True, allow_reuse=True)
    def init_redis_dsn(cls, values):
        return {
            **values,
            "dsn": (
                f"redis://{values['host']}:{values['port']}/{values['db']}"
            ),
        }

    class Config:
        env_prefix = "APP_REDIS_"


class RabbitMQSettings(BaseSettings):
    host: str
    port: int
    username: str
    password: str
    uri: AnyUrl = None

    @root_validator
    def init_rabbitmq_uri(cls, values):
        return {
            **values,
            "uri": (
                f"pyamqp://{values['username']}:{values['password']}"
                f"@{values['host']}:{values['port']}"
            ),
        }

    class Config:
        env_prefix = "APP_RABBITMQ_"


class MLSettings(BaseSettings):
    n_estimators: int = Field(default=100)
    max_depth: int = Field(default=10, ge=1)
    min_samples_leaf: int = Field(default=2, ge=1)
    criterion: Literal["gini", "entropy"] = Field(default="entropy")
    # test_size: confloat(gt=0.0, lt=1.0) = 0.1

    class Config:
        env_prefix = "APP_ML_"


class Settings(BaseSettings):
    redis: RedisSettings = RedisSettings()
    rabbitmq: RabbitMQSettings = RabbitMQSettings()
    ml: MLSettings = MLSettings()


settings = Settings()

# configure logger object
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s | [%(levelname)s] %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
