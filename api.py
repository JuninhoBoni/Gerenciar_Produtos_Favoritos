from services.validate import ValidateToken
from routers import clients, favorites, token
from dependencies import users_db, authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user

from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from datetime import timedelta
from fastapi import Depends, HTTPException, status, FastAPI

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
#async def read_main(current_user: ValidateUser = Depends(get_current_user)):
    return {"msg": "Este projeto não contém front-end"}
