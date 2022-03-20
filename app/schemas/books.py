from datetime import date
from pydantic import BaseModel

# Book Schema
class Books(BaseModel):
    id: int
    isbn: str
    title: str
    author_id: int
    description: str
    publisher_id: int
    publishedDate: date 
    price: float
    copiesSold: int
    genre : str
    rating : int
    