from modules.categoria.repository import CategoriaRepository
from modules.categoria.schemas import CategoriaCreate, Categoria


class CategoriaService:
    def __init__(self, repository: CategoriaRepository = None):
        self.repository = repository or CategoriaRepository()

    def get_categorias(self) -> list[Categoria]:
        categorias = self.repository.get_all()
        return categorias

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