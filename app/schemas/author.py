from pydantic import BaseModel
from models import books
class Author(BaseModel):
    id = int
    firstName = str
    lastName = str

    # Optional
    publisher = str
    biography = str
    books = books
    publisher_id = int