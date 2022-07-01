from fastapi import APIRouter

from .endpoints import datasets

api_router = APIRouter()
api_router.include_router(datasets.router, prefix="/datasets", tags=["datasets"])
