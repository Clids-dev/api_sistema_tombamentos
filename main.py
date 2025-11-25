from fastapi import FastAPI

from api.routes import categoria_route, bem_route, responsavel_routes, setor_routes, movimentacao_routes

app = FastAPI()
app.include_router(bem_route.router)
app.include_router(categoria_route.router)
app.include_router(setor_routes.router)
app.include_router(movimentacao_routes.router)
app.include_router(responsavel_routes.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
