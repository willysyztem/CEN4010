from pydantic import BaseModel

# Credit Card Schema
class CreditCard(BaseModel):
    card_number: str