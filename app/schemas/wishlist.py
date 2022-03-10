from pydantic import BaseModel, EmailStr

# Wish List Schema
class WishList(BaseModel):
    name: str
    books: str

class ShowWishList(BaseModel):
    id: int
    name: str
    books: str
    owner_username: EmailStr

    class Config:
        orm_mode = True