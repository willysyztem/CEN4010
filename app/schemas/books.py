from pydantic import BaseModel

# Book Schema
class Books(BaseModel):
    isbn: str
    title: str
    author_id: int
    description: str
    publisher: str
    publishedDate: str 
    price: float
    copiesSold: int