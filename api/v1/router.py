from fastapi import APIRouter
from modules.bem.router import router as bem_router
from modules.categoria.router import router as categoria_router
from modules.movimentacao.router import router as movimentacao_router
from modules.responsavel.router import router as responsavel_router
from modules.setor.router import router as setor_router
from modules.relatorio.router import router as relatorio_router

api_router = APIRouter()

api_router.include_router(bem_router)
api_router.include_router(categoria_router)
api_router.include_router(movimentacao_router)
api_router.include_router(responsavel_router)
api_router.include_router(setor_router)
api_router.include_router(relatorio_router)
