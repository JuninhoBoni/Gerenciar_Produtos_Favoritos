from routers import clients, favorites, token

from fastapi import FastAPI

tags_metadata = [
    {
        "name": "clients/favorites",
        "description": "Gerenciamento dos Favoritos",
    },
    {
        "name": "clients",
        "description": "Gerenciamento dos Clientes",
    },
    {
        "name": "token",
        "description": "Insira usuário e senha para receber o Token",
    }
]


app = FastAPI(
    title="Produtos Favoritos de Clientes",
    description="Sistema gerenciador de favoritos",
    version="1.0.0",
    openapi_tags=tags_metadata,
)

app.include_router(clients.router)
app.include_router(favorites.router)
app.include_router(token.router)

@app.get("/")
async def read_main():
    return {"msg": "Este projeto não contém front-end"}
