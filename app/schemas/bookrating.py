from pydantic import BaseModel
from datetime import date

# Book Rating
class BookRating(BaseModel):

    id: int
    book: str
    rating: int
    created_at: date

# Book Comments
class BookComment(BaseModel):
    
    id: int
    book: str
    comment: str
    created_at: date