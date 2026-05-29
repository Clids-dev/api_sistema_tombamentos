import unicodedata
from fastapi import HTTPException
from psycopg2 import errors

from modules.categoria.repository import CategoriaRepository
from modules.categoria.schemas import CategoriaCreate, Categoria


class CategoriaService:
    def __init__(self, repository: CategoriaRepository = None):
        self.repository = repository or CategoriaRepository()

    def _normalizar_sigla(self, texto: str) -> str:
        # Remove acentos e caracteres especiais
        nfkd_form = unicodedata.normalize('NFKD', texto)
        return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).upper().strip()

    def get_categorias(self) -> list[Categoria]:
        categorias = self.repository.get_all()
        return categorias

    def create_categoria(self, categoria: CategoriaCreate):
        try:
            categoria.sigla = self._normalizar_sigla(categoria.sigla)
            if categoria.nome.strip() == "":
                raise HTTPException(status_code=400, detail="O nome da categoria não pode ser vazio")
            if categoria.sigla.strip() == "":
                raise HTTPException(status_code=400, detail="A sigla da categoria não pode ser vazia")
            return self.repository.save(categoria)
        except errors.UniqueViolation:
            raise HTTPException(status_code=409, detail=f"A sigla {categoria.sigla} já está em uso")

    def get_categoria_id(self, id: int):
        categoria = self.repository.get_id(id)
        if not categoria:
            raise HTTPException(status_code=404, detail=f"Categoria com id {id} não encontrada")
        return categoria

    def put_categoria(self, id: int, novo_nome: str, nova_sigla: str):
        try:
            nova_sigla = self._normalizar_sigla(nova_sigla)
            return self.repository.put(id, novo_nome, nova_sigla)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Categoria com id {id} não encontrada")
        except errors.UniqueViolation:
            raise HTTPException(status_code=409, detail=f"A sigla {nova_sigla} já está em uso")


    def delete_categoria(self, id: int):
        try:
            return self.repository.delete(id)
        except errors.NoDataFound:
            raise HTTPException(status_code=404, detail=f"Categoria com id {id} não encontrada")
