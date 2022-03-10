from pydantic import BaseModel, EmailStr

# Credit Card Schemas
class CreditCard(BaseModel):
    card_number: str
    owner_username: EmailStr

    class Config:
        orm_mode = True