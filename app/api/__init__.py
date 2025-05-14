from fastapi import APIRouter

from app.api import assistant, vectors

router = APIRouter(prefix="/api")
router.include_router(vectors.router)
router.include_router(assistant.router)
