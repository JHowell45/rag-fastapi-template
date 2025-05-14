from typing import Optional

from chromadb.api.types import Document, QueryResult
from fastapi import APIRouter
from pydantic import BaseModel

from app.dependencies.chroma import ROOT_CHROMA_COLLECTION, ChromaClientDep
from app.dependencies.env import SettingsDep
from app.dependencies.ollama import OllamaClientDep

router = APIRouter(prefix="/assistant", tags=["Assistant"])


class AssistantSearchRequest(BaseModel):
    query: str
    vector_search_count: int = 2


@router.post("/search")
def assistant_search(
    request: AssistantSearchRequest,
    settings: SettingsDep,
    ollama_client: OllamaClientDep,
    chroma_client: ChromaClientDep,
):
    collection = chroma_client.get_or_create_collection(name=ROOT_CHROMA_COLLECTION)
    result: QueryResult = collection.query(
        query_texts=[request.query],  # Chroma will embed this for you
        n_results=request.vector_search_count,  # how many results to return
    )
    documents: Optional[list[list[Document]]] = result.get("documents")
    if documents:
        context = "\n\n".join([doc for docs in documents for doc in docs])
        content = (
            f"with the given cotext: {context} answer the question: {request.query}"
        )
    else:
        content = request.query
    response = ollama_client.chat(
        model=settings.OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": content,
            },
        ],
    )
    print(response)
