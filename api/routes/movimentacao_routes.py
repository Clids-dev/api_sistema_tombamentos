from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from modules.movimentacao.schemas import Movimentacao
from modules.movimentacao.schemas import MovimentacaoCreate
from modules.movimentacao.service import MovimentacaoService

router = APIRouter(prefix="/movimentacao", tags=["Movimentacao"])

@router.get("/", response_model=list[Movimentacao])
def get_movimentacoes():
    service = MovimentacaoService()
    return service.get_movimentacoes()

@router.get("/{id}/", response_model=Optional[schemas.Movimentacao])
def get_movimentacao_by_id(id: int):
    service = MovimentacaoService()
    return service.get_movimentacao_by_id(id)

@router.post("/", response_model=schemas.Movimentacao)
def add_movimentacao(movimentacao: MovimentacaoCreate):
    service = MovimentacaoService()
    return service.add_movimentacao(movimentacao)

@router.put("/{id}")
def update_movimentacao(id: int, data: datetime, setor_destino_id, justificativa: str):
    service = MovimentacaoService()
    return service.put_movimentacao(id, data, setor_destino_id, justificativa)

@router.delete("/")
def delete_movimentacao(id: int):
    service = MovimentacaoService()
    return service.delete_movimentacao(id)
