from pydantic import BaseModel

class Credit_Card_Schema(BaseModel):
    card_number = str
    expiration_date = str
    ccv = str
    card_name = str