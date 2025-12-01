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
