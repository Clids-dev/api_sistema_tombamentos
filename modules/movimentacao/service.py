from datetime import datetime
from fastapi import HTTPException
from psycopg2 import errors

from fastapi import HTTPException
from modules.setor.repository import SetorRepository
from modules.bem.Repository import BemRepository
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
        try:
            if movimentacao.bem_id <= 0 or movimentacao.setor_origem_id <= 0 or movimentacao.setor_destino_id <= 0:
                raise HTTPException(status_code=400, detail="IDs devem ser números positivos.")
            if movimentacao.setor_origem_id == movimentacao.setor_destino_id:
                raise HTTPException(status_code=400, detail="Setor de origem e destino não podem ser iguais.")
            setor_repository = SetorRepository()
            if setor_repository.get_id(movimentacao.setor_origem_id) is None:
                raise HTTPException(status_code=404, detail=f"Setor de origem com id {movimentacao.setor_origem_id} não encontrado")
            if setor_repository.get_id(movimentacao.setor_destino_id) is None:
                raise HTTPException(status_code=404, detail=f"Setor de destino com id {movimentacao.setor_destino_id} não encontrado")
            bem_repository = BemRepository()
            if bem_repository.get_id(movimentacao.bem_id) is None:
                raise HTTPException(status_code=404, detail=f"Bem com id {movimentacao.bem_id} não encontrado")
            repository = MovimentacaoRepository()
            return repository.save(movimentacao)
        except HTTPException as e:
            raise e

    def put_movimentacao(self, id: int, data: datetime, setor_destino_id: int, justificativa=None):
        try:
            repository = MovimentacaoRepository()
            return repository.put(id, data, setor_destino_id, justificativa)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Movimentação com id {id} não encontrada")

    def delete_movimentacao(self, id: int):
        try:
            repository = MovimentacaoRepository()
            return repository.delete(id)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Movimentação com id {id} não encontrada")
