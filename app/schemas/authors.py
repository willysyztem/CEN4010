from pydantic import BaseModel
from models import books

class Authors(BaseModel):
    id = int
    firstName = str
    lastName = str

    # Optional
    publisher = str
    biography = str
    # books = books
    publisher_id = int