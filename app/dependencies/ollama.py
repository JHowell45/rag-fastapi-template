from typing import Annotated

from fastapi import Depends
from ollama import Client

from app.dependencies.env import SettingsDep


def get_ollama_client(settings: SettingsDep) -> Client:
    return Client(host=f"http://{settings.OLLAMA_HOST}:{settings.OLLAMA_PORT}")


OllamaClientDep = Annotated[Client, Depends(get_ollama_client)]
