import fastapi
import uvicorn
from api import clientes, favoritos

tags_metadata = [
    {
        "name": "clientes/favoritos",
        "description": "Gerenciamento dos Favoritos",
    },
    {
        "name": "clientes",
        "description": "Gerenciamento dos Clientes",
    }
]

api = fastapi.FastAPI(
    title="Produtos Favoritos de Clientes",
    description="Sistema gerenciador de favoritos",
    version="1.0.0",
    openapi_tags=tags_metadata,
)


def rotas():
    api.include_router(clientes.router)
    api.include_router(favoritos.router)


if __name__ == '__main__':
    rotas()
    uvicorn.run(api, port=8000, host='127.0.0.1')
