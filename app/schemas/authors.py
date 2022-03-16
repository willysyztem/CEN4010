from pydantic import BaseModel
from models import books

class Authors(BaseModel):
    id = int
    firstName = str
    lastName = str

    # Optional
    publisher_id = int
    biography = str