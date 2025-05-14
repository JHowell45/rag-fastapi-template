from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.dependencies.chroma import ROOT_CHROMA_COLLECTION, ChromaClientDep

router = APIRouter(prefix="/search", tags=["Search"])


class VectorSearchRequest(BaseModel):
    query: str
    result_count: int = Field(default=3)


@router.post("/")
def vector_search(request: VectorSearchRequest, client: ChromaClientDep):
    collection = client.get_or_create_collection(name=ROOT_CHROMA_COLLECTION)
    return collection.query(
        query_texts=[request.query],  # Chroma will embed this for you
        n_results=request.result_count,  # how many results to return
    )
