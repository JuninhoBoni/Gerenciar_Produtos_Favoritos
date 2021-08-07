import fastapi
import uvicorn
from api import clientes

tags_metadata = [
    {
        "name": "criar",
        "description": "Inserir cliente.",
    },
    {
        "name": "atualizar",
        "description": "Atualizar dados do cliente.",
    },
    {
        "name": "visualizar",
        "description": "Mostrar cliente.",
    },
    {
        "name": "remover",
        "description": "Remover cliente.",
    },
]

api = fastapi.FastAPI(
    title="Clientes - Criação, Atualização, Visualização e Remoção",
    description="Sistema gerenciador de clientes",
    version="1.0.0",
    openapi_tags=tags_metadata,
)


def rotas():
    api.include_router(clientes.router)


if __name__ == '__main__':
    rotas()
    uvicorn.run(api, port=8000, host='127.0.0.1')
