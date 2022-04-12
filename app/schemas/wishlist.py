from pydantic import BaseModel

# WishList Schema
class WishList(BaseModel):
    name: str
    
    class Config:
        orm_mode = True

class ShowWishList(BaseModel):
    id: int
    name: str
    owner_id: int
    wishitems: list

# WishItem Schema
class WishItem(BaseModel):
    wishlist_id: int
    book_id: int