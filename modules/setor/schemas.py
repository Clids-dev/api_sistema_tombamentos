from pydantic import BaseModel

from modules.responsavel.schemas import Responsavel


class Setor(BaseModel):
    id: int
    nome: str
    responsavel: Responsavel
    ativo: bool

class SetorCreate(BaseModel):
    nome: str
    responsavel: Responsavel