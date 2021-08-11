from pydantic import BaseModel
from pydantic.networks import EmailStr
from bson.objectid import ObjectId, InvalidId
from typing import Optional


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            ObjectId(str(v))
        except InvalidId as e:
            raise ValueError(f'{e}')
        return ObjectId(str(v))


class ValidateToken(BaseModel):
    access_token: str
    token_type: str


class ValidateTokenData(BaseModel):
    username: Optional[str] = None


class ValidateUser(BaseModel):
    username: str


class ValidateUserDB(ValidateUser):
    hashed_password: str


class ValidateFavorites(BaseModel):
    id_client: ObjectIdStr
    id_product: str


class ValidateFavoritesGet(BaseModel):
    id_client: ObjectIdStr
    id_product: Optional[str] = None


class ValidateCreate(BaseModel):
    name: str
    email: EmailStr


class ValidateUpdate(BaseModel):
    name: str
    email: EmailStr


class ValidateView(BaseModel):
    email: EmailStr


class ValidateRemove(BaseModel):
    email: EmailStr
