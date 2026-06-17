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
        "tipo": tipo,
        "active_page": "bens"
    })

@router.get("/movimentacao")
def tela_movimentacao(request: Request):
    nome = request.cookies.get("username")
    tipo = request.cookies.get("tipo")
    return templates.TemplateResponse("movimentacao.html", {
        "request": request,
        "username": nome,
        "tipo": tipo,
        "active_page": "movimentacao"
    })

@router.get("/categoria")
def tela_categoria(request: Request):
    nome = request.cookies.get("username")
    tipo = request.cookies.get("tipo")
    return templates.TemplateResponse("categoria.html", {
        "request": request,
        "username": nome,
        "tipo": tipo,
        "active_page": "categoria"
    })

@router.get("/setores")
def tela_setores(request: Request):
    nome = request.cookies.get("username")
    tipo = request.cookies.get("tipo")
    return templates.TemplateResponse("setores.html", {
        "request": request,
        "username": nome,
        "tipo": tipo,
        "active_page": "setores"
    })

@router.get("/responsaveis")
def tela_responsaveis(request: Request):
    nome = request.cookies.get("username")
    tipo = request.cookies.get("tipo")
    return templates.TemplateResponse("responsaveis.html", {
        "request": request,
        "username": nome,
        "tipo": tipo,
        "active_page": "responsaveis"
    })

@router.get("/relatorios")
def tela_relatorios(request: Request):
    nome = request.cookies.get("username")
    tipo = request.cookies.get("tipo")
    return templates.TemplateResponse("relatorios.html", {
        "request": request,
        "username": nome,
        "tipo": tipo,
        "active_page": "relatorios"
    })