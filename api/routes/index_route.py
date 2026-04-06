from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request
from modules.bem.service import BemService

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/index")
def get_index(request: Request):
    nome = request.cookies.get("username")
    service = BemService()
    bens_total = service.quantidade_bens()
    bens_ativos = service.quantidade_bens_ativos()
    bens_inativos = service.quantidade_bens_inativos()
    return templates.TemplateResponse(name="index.html",
                                      context=
                                      {"request": request,
                                        "username": nome,
                                        "bens_total": bens_total,
                                        "bens_ativos": bens_ativos,
                                       "bens_inativos": bens_inativos})