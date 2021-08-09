from pydantic import BaseModel
from pydantic.networks import EmailStr
from bson.objectid import ObjectId, InvalidId


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            ObjectId(str(v))
        except InvalidId as e:
            raise ValueError(f'Não é um ObjectId válido - Erro: {e}')
        return ObjectId(str(v))


class ValidarFavoritos(BaseModel):
    id_cliente: ObjectIdStr
    id_produto: str


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
