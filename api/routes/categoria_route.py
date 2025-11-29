from typing import Optional

from fastapi import APIRouter
from modules.categoria import schemas
from modules.categoria.schemas import CategoriaCreate
from modules.categoria.service import CategoriaService

router = APIRouter(prefix="/categoria", tags=["Categoria"])


@router.get("/", response_model=list[schemas.Categoria])
def list_categorias():
    service = CategoriaService()
    return service.get_categorias()


@router.get("/{id}/", response_model=Optional[schemas.Categoria])
def get_categoria_by_id(id: int):
    service = CategoriaService()
    return service.get_categoria_id(id)


@router.post("/", response_model=schemas.Categoria)
def add_categoria(categoria: CategoriaCreate):
    service = CategoriaService()
    return service.create_categoria(categoria)


@router.put("/", response_model=schemas.Categoria)
def update_categoria(id: int, novo_nome: str):
    service = CategoriaService()
    return service.put_categoria(id, novo_nome)


@router.delete("/", response_model=schemas.Categoria)
def delete_categoria(id: int):
    service = CategoriaService()
    return service.delete_categoria(id)
