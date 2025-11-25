from modules.responsavel.repository import ResponsavelRepository
from modules.responsavel.schemas import ResponsavelCreate


class ResponsavelService:
    def get_responsaveis(self):
        repository = ResponsavelRepository()
        return repository.get_all()

    def get_responsavel_by_id(self, id: int):
        repository = ResponsavelRepository()
        return repository.get_id(id)

    def create_responsavel(self, responsavel: ResponsavelCreate):
        repository = ResponsavelRepository()
        return repository.save(responsavel)

    def put_responsavel(self, id: int, novo_nome: str):
        repository = ResponsavelRepository()
        return repository.put(id, novo_nome)

    def delete_responsavel(self, id: int):
        repository = ResponsavelRepository()
        return repository.delete(id)
