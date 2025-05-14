from fastapi import APIRouter

from app.api import vectors

router = APIRouter(prefix="/api")
router.include_router(vectors.router)
