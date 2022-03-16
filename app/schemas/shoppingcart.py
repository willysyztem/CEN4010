from pydantic import BaseModel, EmailStr

# Wish List Schema
class ShoppingCart(BaseModel):
    id: int
    user_id: int
    cart_item_id: int

class ShowShoppingCart(BaseModel):
    id: int
    user_id: int
    cart_item_id: int

    class Config:
        orm_mode = True