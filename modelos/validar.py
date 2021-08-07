from pydantic import BaseModel
from pydantic.networks import EmailStr
from typing import Optional


class ValidarCriar(BaseModel):
    nome: str
    email: EmailStr

class ValidarAtualizar(BaseModel):
    nome: str
    email: EmailStr

class ValidarVisualizar(BaseModel):
    nome: Optional[str]
    email: Optional[str]

class ValidarRemover(BaseModel):
    email: EmailStr
