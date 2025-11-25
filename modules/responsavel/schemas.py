from pydantic import BaseModel


class Responsavel(BaseModel):
    id: int
    nome: str
    cargo: str
    ativo: bool


class ResponsavelCreate(BaseModel):
    nome: str
    cargo: str