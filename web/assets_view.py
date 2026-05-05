from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/bens")
def tela_bens(request: Request):
    nome = request.cookies.get("username")
    tipo = request.cookies.get("tipo")
    return templates.TemplateResponse("bens.html", {
        "request": request,
        "username": nome,
        "tipo": tipo
    })