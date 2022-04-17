from datetime import date
from pydantic import BaseModel

# Book Schema
class Books(BaseModel):
    isbn: str
    title: str
    author_id: int
    description: str
    publisher_id: int
    published_date: date 
    price: float
    copies_sold: int
    genre: str
    pages: int