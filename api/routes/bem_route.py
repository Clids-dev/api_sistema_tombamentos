from typing import Optional

from fastapi import APIRouter
from fastapi.params import Depends

from core.db import DataBase
from modules.bem import schemas
from modules.bem.schemas import BemCreate
from modules.bem.service import BemService

router = APIRouter(prefix="/bem", tags=["Bem"])

@router.post("/", response_model=schemas.Bem)
def add_bem(bem: BemCreate):
    service = BemService()
    return service.create_bem(bem)

@router.get("/", response_model=list[schemas.Bem])
def get_bens():
    service = BemService()
    return service.get_bens()

@router.get("/{id}/", response_model=Optional[schemas.Bem])
def get_bem_by_id(id: int):
    service = BemService()
    return service.get_bem_by_id(id)

@router.put("/{id}/", response_model=Optional[schemas.Bem])
def update_bem(id : int, nome: str, status: str):
    service = BemService()
    return service.put_bem(id, nome, status)