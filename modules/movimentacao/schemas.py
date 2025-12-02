from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Movimentacao(BaseModel):
    id: int
    bem_id: int
    setor_origem_id: Optional[int] = None
    setor_destino_id: int
    data: datetime
    justificativa: Optional[str] = None
    ativo: bool


class MovimentacaoCreate(BaseModel):
    bem_id: int
    setor_origem_id: Optional[int] = None
    setor_destino_id: int

class MovimentacaoUpdate(BaseModel):
    setor_destino_id: int
    data: datetime
    justificativa: Optional[str] = None