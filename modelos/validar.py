from pydantic import BaseModel
from pydantic.networks import EmailStr


class ValidarChave(BaseModel):
    chave: str


class ValidarCriar(BaseModel):
    nome: str
    email: EmailStr


class ValidarAtualizar(BaseModel):
    nome: str
    email: EmailStr


class ValidarVisualizar(BaseModel):
    email: str


class ValidarRemover(BaseModel):
    email: EmailStr
