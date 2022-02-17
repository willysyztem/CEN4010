from typing import Optional
from pydantic import BaseModel, EmailStr

class User_Schema(BaseModel):
    # email is username as well
    email: EmailStr
    password: str

    # Optional Fields To Project Specs
    name: Optional[str]
    home_address: Optional[str]