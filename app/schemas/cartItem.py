from pydantic import BaseModel

# Book Schema
class cartItem(BaseModel):
    id: int
    shoppingcart_id = int
    book_id = int
    book_title = str