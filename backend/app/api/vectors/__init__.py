from fastapi import APIRouter
from pydantic import BaseModel

from app.api.vectors import collections, search, store
from app.dependencies.chroma import ChromaClientDep

router = APIRouter(prefix="/vector", tags=["Vectors"])

router.include_router(store.router)
router.include_router(collections.router)
router.include_router(search.router)


class ChromaHeartbeatResponse(BaseModel):
    heartbeat: int


@router.get("/hearbeat", response_model=ChromaHeartbeatResponse)
def chroma_heartbeat(client: ChromaClientDep) -> ChromaHeartbeatResponse:
    return ChromaHeartbeatResponse(heartbeat=client.heartbeat())
