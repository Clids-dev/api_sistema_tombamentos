from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request
from modules.bem.service import BemService
from modules.categoria.service import CategoriaService

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/index")
def get_index(request: Request):
    nome = request.cookies.get("username")
    tipo = request.cookies.get("tipo")

    service = BemService()
    cat_service = CategoriaService()
    
    bens_total = service.quantidade_bens()
    bens_ativos = service.quantidade_bens_ativos()
    bens_inativos = service.quantidade_bens_inativos()

    recentes_raw = service.bens_recentes()
    # Pega até 3 nomes, ou preenche com "---" se não houver
    recente1 = recentes_raw[0][1] if len(recentes_raw) > 0 else "---"
    recente2 = recentes_raw[1][1] if len(recentes_raw) > 1 else "---"
    recente3 = recentes_raw[2][1] if len(recentes_raw) > 2 else "---"

    categorias = cat_service.get_categorias()

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
            "recente3": recente3,
            "categorias": categorias,
            "active_page": "index"
        }
    )
