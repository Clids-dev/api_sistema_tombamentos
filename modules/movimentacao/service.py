from datetime import datetime
from fastapi import HTTPException
from psycopg2 import errors

from modules.movimentacao.repository import MovimentacaoRepository
from modules.movimentacao.schemas import MovimentacaoCreate


class MovimentacaoService:
    def get_movimentacoes(self):
        repository = MovimentacaoRepository()
        return repository.get_all()

    def get_movimentacao_by_id(self, id: int):
        repository = MovimentacaoRepository()
        return repository.get_id(id)

    def add_movimentacao(self, movimentacao: MovimentacaoCreate):
        repository = MovimentacaoRepository()
        return repository.save(movimentacao)

    def put_movimentacao(self, id: int, data: datetime, setor_destino_id: int):
        try:
            repository = MovimentacaoRepository()
            return repository.put(id, data, setor_destino_id)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Movimentação com id {id} não encontrada")

    def delete_movimentacao(self, id: int):
        try:
            repository = MovimentacaoRepository()
            return repository.delete(id)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Movimentação com id {id} não encontrada")