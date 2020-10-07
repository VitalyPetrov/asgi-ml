import os
from pathlib import Path
from pydantic import validator, BaseSettings
from dotenv import load_dotenv


PROJECT_ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
load_dotenv()


class MLSettings(BaseSettings):
    pass


class Settings(BaseSettings):
    api_prefix: str = os.getenv("APP_API_PREFIX")

    @validator("api_prefix", pre=True)
    def is_valid_api_prefix(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError(
                f"API prefix should have str type, got {type(value)} instead"
            )
        return value


settings = Settings()
