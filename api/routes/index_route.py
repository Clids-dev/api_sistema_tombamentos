from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request
from modules.bem.service import BemService

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/index")
def get_index(request: Request):
    nome = request.cookies.get("username")
    tipo = request.cookies.get("tipo")

    service = BemService()
    bens_total = service.quantidade_bens()
    bens_ativos = service.quantidade_bens_ativos()
    bens_inativos = service.quantidade_bens_inativos()

    recente1 = service.bens_recentes()[0][1]
    recente2 = service.bens_recentes()[1][1]
    recente3 = service.bens_recentes()[2][1]

    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
            "username": nome,
            "tipo": tipo,  
            "bens_total": bens_total,
            "bens_ativos": bens_ativos,
            "bens_inativos": bens_inativos,
            "recente1": recente1,
            "recente2": recente2,
            "recente3": recente3
        }
    )