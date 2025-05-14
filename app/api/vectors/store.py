from fastapi import APIRouter
from pydantic import BaseModel

from app.dependencies.chroma import ChromaClientDep

router = APIRouter(prefix="/store")


class StoreVectorRequest(BaseModel):
    vector: list[float]


class StoreTextRequest(BaseModel):
    text: str


@router.post("/vector")
def store_vector(request: StoreVectorRequest, client: ChromaClientDep):
    pass


@router.post("/text")
def store_text(request: StoreTextRequest, client: ChromaClientDep):
    pass
