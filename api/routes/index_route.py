from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/index")
def get_index(request: Request):
    nome = request.cookies.get("username")
    return templates.TemplateResponse(name="index.html",
                                      context=
                                      {"request": request,
                                      "username": nome})