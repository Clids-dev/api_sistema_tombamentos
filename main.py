
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routes import bensView_route, categoria_route, bem_route, responsavel_routes, setor_routes, movimentacao_routes, login_route, \
    index_route

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(login_route.router)
app.include_router(index_route.router)
app.include_router(bensView_route.router)
app.include_router(bem_route.router)
app.include_router(categoria_route.router)
app.include_router(setor_routes.router)
app.include_router(movimentacao_routes.router)
app.include_router(responsavel_routes.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}