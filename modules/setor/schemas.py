from pydantic import BaseModel

from modules.responsavel.schemas import Responsavel


class Setor(BaseModel):
    id: int
    nome: str
    responsavel_id: int
    ativo: bool

class SetorCreate(BaseModel):
    nome: str
    responsavel_id: int

class SetorFlat(BaseModel):
    id_setor: int
    setor: str
    id_responsavel: int
    responsavel: str
    cargo_responsavel: str
    ativo: bool