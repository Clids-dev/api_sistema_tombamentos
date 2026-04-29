from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Bem(BaseModel):
    id: int
    nome: str
    codigo_tombamento: str
    valor: float
    status: str
    ativo: bool

class BemCreate(BaseModel):
    nome: str
    codigo_tombamento: str
    valor: float
    status: str

class BemDeleteResponse(BaseModel):
    message: str
    id: int
    ativo: bool

class BemDetalhes(Bem):
    setor_atual: Optional[str] = None
    data_ultima_movimentacao: Optional[datetime] = None
    justificativa: Optional[str] = None

