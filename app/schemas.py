from typing import Optional
from pydantic import BaseModel, EmailStr

# Oauth2 Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]

# User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# User Schemas
class User(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str]
    home_address: Optional[str]

class ShowUser(BaseModel):
    id: int
    username: EmailStr
    email: EmailStr
    name: str
    home_address: str

    class Config:
        orm_mode = True


class CreditCard(BaseModel):
    card_number: str
    owner_username: EmailStr

    class Config:
        orm_mode = True
