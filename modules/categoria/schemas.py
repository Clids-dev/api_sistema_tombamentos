from pydantic import BaseModel
from typing import Optional


class Categoria(BaseModel):
    id: int
    nome: str
    sigla: str
    ativo: bool


class CategoriaCreate(BaseModel):
    nome: str
    sigla: str
