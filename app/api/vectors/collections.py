from fastapi import APIRouter
from pydantic import BaseModel

from app.dependencies.chroma import ChromaClientDep

router = APIRouter(prefix="/collections")


class ShowCollectionResponse(BaseModel):
    collections: list[str]


class CreateCollectionRequest(BaseModel):
    name: str


@router.get("/show", response_model=ShowCollectionResponse)
def show_collection(client: ChromaClientDep) -> ShowCollectionResponse:
    return ShowCollectionResponse(collections=client.list_collections())


@router.post("/create")
def create_collection(request: CreateCollectionRequest, client: ChromaClientDep):
    client.get_or_create_collection(name=request.name)
    return {"ok": True}
