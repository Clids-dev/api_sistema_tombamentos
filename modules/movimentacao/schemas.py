from datetime import datetime

from pydantic import BaseModel


class Movimentacao(BaseModel):
    id: int
    bem_id: int
    setor_origem_id: int | None = None
    setor_destino_id: int | None = None
    data: datetime
    ativo: bool


class MovimentacaoCreate(BaseModel):
    bem_id: int
    setor_origem_id: int
    setor_destino_id: int
