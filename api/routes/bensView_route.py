from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/bens")
def tela_bens(request: Request):
    return templates.TemplateResponse("bens.html", {
        "request": request
    })