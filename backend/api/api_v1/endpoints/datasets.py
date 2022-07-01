from typing import List

from fastapi import APIRouter

from backend import schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def integrate_datasets():
    pass
