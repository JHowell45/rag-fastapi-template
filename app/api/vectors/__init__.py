from fastapi import APIRouter

from app.api.vectors import collections, store

router = APIRouter(prefix="/vector", tags=["Vectors"])

router.include_router(store.router)
router.include_router(collections.router)
