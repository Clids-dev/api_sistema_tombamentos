from fastapi import HTTPException
from psycopg2 import errors

from modules.categoria.repository import CategoriaRepository
from modules.categoria.schemas import CategoriaCreate, Categoria


class CategoriaService:
    def __init__(self, repository: CategoriaRepository = None):
        self.repository = repository or CategoriaRepository()

    def get_categorias(self) -> list[Categoria]:
        categorias = self.repository.get_all()
        return categorias

    def create_categoria(self, categoria: CategoriaCreate):
        try:
            repository = CategoriaRepository()
            return repository.save(categoria)
        except errors.UniqueViolation:
            raise HTTPException(status_code=409, detail=f"Categoria {categoria.nome} já existe")

    def get_categoria_id(self, id: int):
        repository = CategoriaRepository()
        categoria = repository.get_id(id)
        return categoria

    def put_categoria(self,id: int, novo_nome: str):
        try:
            if novo_nome == self.get_categoria_id(id).nome:
                raise ValueError
            repository = CategoriaRepository()
            return repository.put(id, novo_nome)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Categoria com id {id} não encontrada")
        except errors.UniqueViolation:
            raise HTTPException(status_code=409, detail=f"Categoria {novo_nome} já existe")
        except ValueError:
            raise HTTPException(status_code=400, detail="O novo nome é igual ao nome atual da categoria")


    def delete_categoria(self, id: int):
        try:
            repository = CategoriaRepository()
            return repository.delete(id)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Categoria com id {id} não encontrada")