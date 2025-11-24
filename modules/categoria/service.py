from modules.categoria.repository import CategoriaRepository
from modules.categoria.schemas import CategoriaCreate


class CategoriaService:
    def get_categorias(self):
        repository = CategoriaRepository()
        return repository.get_all()

    def create_categoria(self, categoria: CategoriaCreate):
        repository = CategoriaRepository()
        return repository.save(categoria)

    def get_categoria_id(self, id: int):
        repository = CategoriaRepository()
        categoria = repository.get_id(id)
        return categoria

    def put_categoria(self,id: int, novo_nome: str):
        repository = CategoriaRepository()
        categoria = repository.put(id, novo_nome)
        return categoria

    def delete_categoria(self, id: int):
        repository = CategoriaRepository()
        categoria = repository.delete(id)
        return categoria