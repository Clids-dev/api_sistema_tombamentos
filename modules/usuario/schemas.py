from pydantic import BaseModel

class UsuarioLogin(BaseModel):
    username: str
    senha: str

class UsuarioResponse(BaseModel):
    id: int
    username: str
    tipo: str
    ativo: bool