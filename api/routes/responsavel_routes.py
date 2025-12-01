from typing import Optional

from fastapi import APIRouter
from modules.responsavel.schemas import Responsavel
from modules.responsavel.schemas import ResponsavelCreate
from modules.responsavel.service import ResponsavelService

router = APIRouter(prefix="/responsavel", tags=["Responsavel"])

@router.get("/", response_model=list[Responsavel])
def get_responsaveis():
    service = ResponsavelService()
    return service.get_responsaveis()

@router.get("/{id}/", response_model=Responsavel)
def get_responsavel_by_id(id: int):
    service = ResponsavelService()
    return service.get_responsavel_by_id(id)

@router.post("/", response_model=ResponsavelCreate)
def add_responsavel(responsavel: ResponsavelCreate):
    service = ResponsavelService()
    return service.create_responsavel(responsavel)

@router.put("/", response_model=ResponsavelCreate)
def put_responsavel(id: int, dados: ResponsavelCreate):
    service = ResponsavelService()
    return service.put_responsavel(id, dados.nome, dados.cargo)

@router.delete("/", response_model=Responsavel)
def delete_responsavel(id: int):
    service = ResponsavelService()
    return service.delete_responsavel(id)



