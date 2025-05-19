from hashlib import sha256

from fastapi import APIRouter
from pydantic import BaseModel

from app.dependencies.chroma import ROOT_CHROMA_COLLECTION, ChromaClientDep

router = APIRouter(prefix="/store", tags=["store"])


class StoreTextRequest(BaseModel):
    text: str

    @property
    def id(self) -> str:
        return sha256(self.text.encode()).hexdigest()


@router.post("/text")
def store_text(request: StoreTextRequest, client: ChromaClientDep):
    collection = client.get_or_create_collection(name=ROOT_CHROMA_COLLECTION)
    collection.upsert(documents=[request.text], ids=[request.id])
    return {"ok": True}
