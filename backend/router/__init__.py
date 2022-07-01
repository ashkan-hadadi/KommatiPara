from fastapi import APIRouter

from backend.api.api_v1.api import api_router
from . import healthcheck


router = APIRouter()

router.include_router(
    healthcheck.router,
    prefix='/healthcheck',
    tags=['Healthcheck']
)
router.include_router(
    api_router
)
