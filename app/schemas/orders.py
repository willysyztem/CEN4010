from datetime import date
from pydantic import BaseModel

# Order Schema
class Orders(BaseModel):
    id : int
    user_id : int
    orderDate : date
    subtotal : int
    shipping :  int