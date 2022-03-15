from sqlite3 import Date
from pydantic import BaseModel

class Orders(BaseModel):
    id = int
    user_id = int
    orderDate = Date
    subtotal = int
    shipping = int