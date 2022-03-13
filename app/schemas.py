from datetime import datetime
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
    created_at: datetime

    class Config:
        orm_mode = True

# Credit Card Schemas
class CreditCard(BaseModel):
    card_number: str
    owner_username: EmailStr

    class Config:
        orm_mode = True

# Wish List Schema
class WishList(BaseModel):
    name: str
    books: str

class ShowWishList(BaseModel):
    id: int
    name: str
    books: str
    owner_username: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    ratings: int

    class Config:
        orm_mode = True

class Rate(BaseModel):
    post_id: int
    dir: conint(le=1)