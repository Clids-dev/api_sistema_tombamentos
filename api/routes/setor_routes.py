from fastapi import APIRouter
from modules.setor import schemas
from modules.setor.schemas import SetorCreate
from modules.setor.service import SetorService

router = APIRouter(prefix="/setores", tags=["Setores"])

@router.get("/", response_model=schemas)
def get_setores():
    service = SetorService()
    return service.get_setores()

@router.get("/", response_model=schemas)
def get_setor_by_id(id: int):
    service = SetorService()
    return service.get_setor_by_id(id)
@router.post("/", response_model=schemas)
def add_setor(setor: SetorCreate):
    service = SetorService()
    return service.add_setor(setor)

@router.put("/", response_model=schemas)
def update_setor(id: int, novo_nome: str):
    service = SetorService()
    return service.put_setor(id, novo_nome)

router.delete("/", response_model=schemas)
def delete_setor(id: int):
    service = SetorService()
    return service.delete_setor(id)