from pydantic import BaseModel, EmailStr

# Wish List Schema
class ShoppingCart(BaseModel):
    username: str
    books: str

class ShowShoppingCart(BaseModel):
    user_id: int
    username: str
    books: str
    book_id: int

    class Config:
        orm_mode = True