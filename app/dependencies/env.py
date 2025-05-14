from typing import Annotated

from fastapi import Depends
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


def get_env_settings() -> Settings:
    return Settings()


SeetingsDep = Annotated[Settings, Depends(get_env_settings)]
