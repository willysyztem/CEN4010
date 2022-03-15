from pydantic import BaseModel

# Wish List Schema
class WishList(BaseModel):
    name: str
    books: str

class ShowWishList(BaseModel):
    id: int
    name: str
    books: str
    user_id: int