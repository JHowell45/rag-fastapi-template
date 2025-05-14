from typing import Annotated

from fastapi import Depends
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #######################################
    # Ollama
    #######################################
    OLLAMA_HOST: str = Field(default="ollama")
    OLLAMA_PORT: int = Field(default=11434)

    #######################################
    # ChromaDB
    #######################################
    CHROMADB_HOST: str = Field(default="vdb")
    CHROMADB_PORT: int = Field(default=8000)

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


def get_env_settings() -> Settings:
    return Settings()


SettingsDep = Annotated[Settings, Depends(get_env_settings)]
