from typing import Optional
from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    email: EmailStr
    password: str

    # Optional Fields To Project Specs
    name: Optional[str]
    home_address: Optional[str]
