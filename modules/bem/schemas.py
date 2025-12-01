from pydantic import BaseModel

class Bem(BaseModel):
    id: int
    nome: str
    codigo_tombamento: str
    valor: float
    status: str
    ativo: bool

class BemUpdate(BaseModel):
    id: int
    nome: str
    status: str

class BemCreate(BaseModel):
    nome: str
    codigo_tombamento: str
    valor: float
    status: str
