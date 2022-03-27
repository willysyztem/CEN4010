from typing import Optional
from pydantic import BaseModel

# Oauth2 Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]