from modules.setor.repository import SetorRepository
from modules.setor.schemas import SetorCreate


class SetorService:
    def get_setores(self):
        repository = SetorRepository()
        return repository.get_all()

    def get_setor_by_id(self, id: int):
        repository = SetorRepository()
        return repository.get_all()

    def add_setor(self, setor: SetorCreate):
        repository = SetorRepository()
        return repository.save(setor)

    def put_setor(self, id: int, novo_nome: str):
        repository = SetorRepository()
        return repository.put(id, novo_nome)

    def delete_setor(self, id: int):
        repository = SetorRepository()
        return repository.delete(id)