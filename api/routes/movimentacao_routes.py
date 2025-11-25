import datetime

from fastapi import APIRouter
from modules.movimentacao import schemas
from modules.movimentacao.schemas import MovimentacaoCreate
from modules.movimentacao.service import MovimentacaoService

router = APIRouter(prefix="/movimentacao", tags=["Movimentacao"])

@router.get("/", response_model=schemas)
def get_movimentacoes():
    service = MovimentacaoService()
    return service.get_movimentacoes()

@router.get("/", response_model=schemas)
def get_movimentacao_by_id(id: int):
    service = MovimentacaoService()
    return service.get_movimentacao_by_id(id)

@router.post("/", response_model=schemas)
def add_movimentacao(movimentacao: MovimentacaoCreate):
    service = MovimentacaoService()
    return service.add_movimentacao(movimentacao)

@router.put("/", response_model=schemas)
def update_movimentacao(id: int, data: datetime, setor_destino_id):
    service = MovimentacaoService()
    return service.put_movimentacao(id, data, setor_destino_id)

def delete_movimentacao(id: int):
    service = MovimentacaoService()
    return service.delete_movimentacao(id)
