from pydantic import BaseModel

# Book Schema
class BookSchema(BaseModel):
    isbn: str
    title: str
    author_id: int
    description: str
    publisher: str
    publishedDate: str 
    price: float
    copiesSold: int