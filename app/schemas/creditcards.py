from pydantic import BaseModel

# Credit Card Schemas
class CreditCards(BaseModel):
    card_number: str
    user_id: int

    class Config:
        orm_mode = True