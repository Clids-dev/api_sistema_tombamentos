from pydantic import BaseModel
from typing import Optional

from modules.responsavel.schemas import Responsavel


class Setor(BaseModel):
    id: int
    nome: str
    responsavel_id: int
    flag_almoxarifado: bool = False
    ativo: bool

class SetorCreate(BaseModel):
    nome: str
    responsavel_id: int
    flag_almoxarifado: bool = False

class SetorFlat(BaseModel):
    id_setor: int
    setor: str
    id_responsavel: Optional[int] = None
    responsavel: Optional[str] = None
    cargo_responsavel: Optional[str] = None
    flag_almoxarifado: bool = False
