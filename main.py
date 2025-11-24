from fastapi import FastAPI

from api.routes import categoria_route, bem_route

app = FastAPI()
app.include_router(bem_route.router)
app.include_router(categoria_route.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
