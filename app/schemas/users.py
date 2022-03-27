from typing import Optional
from pydantic import BaseModel, EmailStr

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
    password: str
    name: Optional[str]
    home_address: Optional[str]

class ShowUser(BaseModel):
    id: int
    username: EmailStr
    email: EmailStr
    name: Optional[str]
    home_address: Optional[str]

    class Config:
        orm_mode = True