from typing import Annotated

import chromadb
from chromadb import ClientAPI
from fastapi import Depends


def get_chroma_client() -> ClientAPI:
    return chromadb.HttpClient(host="vdb", port=8000)


ChromaClientDep = Annotated[ClientAPI, Depends[get_chroma_client]]
