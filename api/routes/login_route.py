from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from core.db import DataBase
from modules.usuario.repository import UsuarioRepository
from modules.usuario.service import UsuarioService

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# GET - página de login
@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# POST - processar login
@router.post("/login")
def login(
    request: Request,
    login_usuario: str = Form(...),
    password_usuario: str = Form(...)
):
    db = DataBase()
    repo = UsuarioRepository(db)
    service = UsuarioService(repo)

    user = service.login(login_usuario, password_usuario)

    if not user:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "erro": "Login inválido"
        })
    response = RedirectResponse(url="/index", status_code=302)

    response.set_cookie(key="username", value=user[1])
    response.set_cookie(key="tipo", value=user[3])

    return response