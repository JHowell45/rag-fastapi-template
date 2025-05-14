from typing import Annotated

import chromadb
from chromadb import ClientAPI
from chromadb.config import Settings
from fastapi import Depends

from app.dependencies.env import SettingsDep

ROOT_CHROMA_COLLECTION: str = "documents"


def get_chroma_client(settings: SettingsDep) -> ClientAPI:
    return chromadb.HttpClient(
        host=settings.CHROMADB_HOST,
        port=settings.CHROMADB_PORT,
        settings=Settings(anonymized_telemetry=False),
    )


ChromaClientDep = Annotated[ClientAPI, Depends(get_chroma_client)]
