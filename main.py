from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.v1.router import api_router
from web.router import web_router

app = FastAPI(
    title="Sistema de Tombamento",
    description="API e Interface Web para gestão de patrimônio",
    version="1.0.0"
)

# Arquivos Estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Rotas Web (Templates)
app.include_router(web_router)

# Rotas API (JSON)
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Bem-vindo ao Sistema de Tombamento. Acesse /index para a interface web ou /docs para a API."}
