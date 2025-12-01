from modules.bem.Repository import BemRepository
from modules.bem.schemas import BemCreate

from psycopg2 import errors
from fastapi import HTTPException

class BemService:
    def get_bens(self):
        repository = BemRepository()
        return repository.get_all()

    def get_bem_by_id(self, id: int):
        repository = BemRepository()
        return repository.get_by_id(id)

    def create_bem(self, bem : BemCreate):
        repository = BemRepository()
        return repository.save(bem)

    def put_bem(self, id: int, novo_nome: str, status: str):
        try:
            repository = BemRepository()
            return repository.put(id, novo_nome, status)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Bem com id {id} não encontrada")
        except errors.UniqueViolation:
            raise HTTPException(status_code=409, detail=f"Bem {novo_nome} já existe")

    def delete_bem(self, id: int):
        try:
            repository = BemRepository()
            return repository.delete(id)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Categoria com id {id} não encontrada")