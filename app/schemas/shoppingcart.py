from pydantic import BaseModel

# ShoppingCart Schema
class ShoppingCart(BaseModel):
    id: int
    user_id: int
    cartitems: list = None

# CartItem Schema
class CartItem(BaseModel):
    book_id: int

class ShowCartItem(BaseModel):
    shoppingcart_id: int
    bookd_id: int

    class Config:
        orm_mode = True