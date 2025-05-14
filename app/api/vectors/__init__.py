from fastapi import APIRouter

from app.api.vectors import store

router = APIRouter(prefix="/vector", tags=["Vectors"])

router.include_router(store.router)
