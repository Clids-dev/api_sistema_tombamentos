from datetime import datetime

from modules.movimentacao.repository import MovimentacaoRepository
from modules.movimentacao.schemas import MovimentacaoCreate


class MovimentacaoService:
    def get_movimentacoes(self):
        repository = MovimentacaoRepository()
        return repository.get_all()

    def get_movimentacao_by_id(self, id: int):
        repository = MovimentacaoRepository()
        return repository.get_id()

    def add_movimentacao(self, movimentacao: MovimentacaoCreate):
        repository = MovimentacaoRepository()
        return repository.save(movimentacao)

    def put_movimentacao(self, id: int, data: datetime, setor_destino_id: int):
        repository = MovimentacaoRepository()
        return repository.put(id, data, setor_destino_id)

    def delete_movimentacao(self, id: int):
        repository = MovimentacaoRepository()
        return repository.delete(id)