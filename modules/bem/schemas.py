from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Bem(BaseModel):
    id: int
    nome: str
    tipo: str
    codigo_tombamento: str
    valor: float
    status: str
    ativo: bool
    id_categoria: Optional[int] = None

class BemCreate(BaseModel):
    nome: str
    tipo: str
    valor: float
    status: str
    id_categoria: int

class BemDeleteResponse(BaseModel):
    message: str
    id: int
    ativo: bool

class BemDetalhes(Bem):
    setor_atual: Optional[str] = None
    id_setor_atual: Optional[int] = None
    data_ultima_movimentacao: Optional[datetime] = None
    justificativa: Optional[str] = None
    categoria_nome: Optional[str] = None
