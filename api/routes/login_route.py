from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

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
    
    print("=== LOGIN RECEBIDO ===")
    print("Usuário:", login_usuario)

    db = DataBase()
    repo = UsuarioRepository(db)
    service = UsuarioService(repo)

    try:
        user = service.login(login_usuario, password_usuario)

        if not user:
            print("❌ Login inválido")

            return templates.TemplateResponse("login.html", {
                "request": request,
                "erro": "Login inválido"
            })

        print("✅ Login válido!")
        print("Tipo:", user[3])

        return templates.TemplateResponse("login.html", {
            "request": request,
            "sucesso": "Login realizado com sucesso"
        })

    except Exception as e:
        print("🔥 ERRO:", e)
        db.conn.rollback()

        return templates.TemplateResponse("login.html", {
            "request": request,
            "erro": "Erro interno no servidor"
        })

    finally:
        db.conn.close()  # 🔥 garante que sempre fecha