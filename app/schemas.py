from typing import Optional
from pydantic import BaseModel, EmailStr

# User Schemas
class User(BaseModel):
    email: EmailStr
    password: str
    name: Optional[str]
    home_address: Optional[str]

class ShowUser(BaseModel):
    email: EmailStr
    username: EmailStr
    name: str
    home_address: str
    class Config():
        orm_mode = True