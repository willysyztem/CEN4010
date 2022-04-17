from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr
from fastapi import Form

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

class UpdateUser(BaseModel):
    password: Optional[str]
    name: Optional[str]
    home_address: Optional[str]

class ShowUser(BaseModel):
    id: int
    username: EmailStr
    email: EmailStr
    name: Optional[str]
    home_address: Optional[str]
    date_created: date

    class Config:
        orm_mode = True