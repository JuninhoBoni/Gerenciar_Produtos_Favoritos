from services.validate import ValidateToken, ValidateOAuth2PasswordRequestForm
import uvicorn
from datetime import timedelta
from fastapi import Depends, HTTPException, status
from routers import clients, favorites
from fastapi import FastAPI
from dependencies import fake_users_db, authenticate_user, create_access_token
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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


@app.post("/token", response_model=ValidateToken, tags=['token'])
async def login_for_access_token(form_data: ValidateOAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(
        fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def rotas():
    app.include_router(clients.router)
    app.include_router(favorites.router)


if __name__ == '__main__':
    rotas()
    uvicorn.run(app, port=8000, host='0.0.0.0')
