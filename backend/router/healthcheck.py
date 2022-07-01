from fastapi import APIRouter
from fastapi import Request


router = APIRouter()


@router.get('/readiness')
async def readiness(request: Request) -> dict:
    return {'status': 'ok'}


@router.get('/liveness')
async def liveness(request: Request) -> dict:
    return {'status': 'ok'}


@router.get('/startup')
async def startup(request: Request) -> dict:
    return {'status': 'ok'}
