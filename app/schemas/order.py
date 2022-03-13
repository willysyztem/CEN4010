from sqlite3 import Date
from pydantic import BaseModel

class Order(BaseModel):
    id = int
    user_id = int
    orderDate = Date
    subtotal = int
    shipping = int