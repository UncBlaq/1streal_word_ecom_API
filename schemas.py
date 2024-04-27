from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
class ShowProduct(BaseModel):
    name : str
    price : Decimal
    qauntity_available : int
    # class Config():
    #     orm_mode = True

class ShowUser(BaseModel):
    email: str
    products: list[ShowProduct] = []

class UserBase(BaseModel):
    email: str

class Product(BaseModel):
    name : str
    price : Decimal
    qauntity_available : int
    owner : UserBase


class User(BaseModel):
    email: str
    password: str


class Login(BaseModel):
    email: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None