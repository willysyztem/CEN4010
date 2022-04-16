from pydantic import BaseModel, Field
from datetime import date

# Book Rating
class BookRating(BaseModel):

    user_id: str
    book: str
    rating: int = Field(None, gt=1, lt=5)
    created_at: date

# Book Comments
class BookComment(BaseModel):
    
    user_id: str
    book: str
    comment: str
    created_at: date