from typing import Optional

from fastapi import APIRouter
from modules.bem import schemas
from modules.bem.schemas import BemCreate
from modules.bem.service import BemService

router = APIRouter(prefix="/bem", tags=["Bem"])

@router.get("/", response_model=list[schemas.Bem])
def list_bens():
    service = BemService()
    return service.get_bens()

@router.get("/", response_model=Optional[schemas.Bem])
def get_bem_by_id(id: int):
    service = BemService()
    return service.get_bem_by_id(id)

@router.post("/", response_model=list[schemas.Bem])
def add_bem(bem: BemCreate):
    service = BemService()
    return service.create_bem(bem)
