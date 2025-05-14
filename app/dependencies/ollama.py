from typing import Annotated

from fastapi import Depends
from ollama import Client


def get_ollama_client() -> Client:
    return Client(host="http://ollama:11434")


OllamaClientDep = Annotated[Client, Depends(get_ollama_client)]
