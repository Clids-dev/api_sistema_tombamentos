from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.params import Depends

from core.db import DataBase
from modules.bem import schemas
from modules.bem.schemas import BemCreate, BemDeleteResponse
from modules.bem.service import BemService
from modules.movimentacao.schemas import Movimentacao

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

@router.delete("/{id}/", response_model=BemDeleteResponse)
def delete_bem(id: int):
    service = BemService()
    try:
        bem = service.delete_bem(id)
        return {
            "message": "Bem desativado com sucesso",
            "id": bem.id,
            "ativo": bem.ativo
        }
    except HTTPException as e:
        raise e

@router.get("/buscar", response_model=schemas.Bem)
def buscar_bem_por_codigo(codigo_tombamento: str):
    service = BemService()
    return service.get_by_codTomb(codigo_tombamento)

@router.get("/{id}/historico-movimentacoes", response_model=list[Movimentacao])
def get_historico_by_bem_id(id: int):
    service = BemService()
    return service.get_historico_by_bem(id)

@router.get("/por-setor", response_model=list[schemas.Bem])
def listar_bens_por_setor(setor_id: int):
    service = BemService()
    return service.get_por_setor(setor_id)

@router.post("/{id}/desativar")
def desativar_bem(id: int):
    service = BemService()
    return service.desativar_bem(id)


@router.post("/{id}/reativar")
def reativar_bem(id: int):
    service = BemService()
    return service.reativar_bem(id)

@router.get("/relatorios/bens-ativos-por-status")
def bens_ativos_por_status():
    service = BemService()
    return service.bens_ativos_por_status()
