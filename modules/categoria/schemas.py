from pydantic import BaseModel


class Categoria(BaseModel):
    id: int
    nome: str
    ativo: bool


class CategoriaCreate(BaseModel):
    nome: int