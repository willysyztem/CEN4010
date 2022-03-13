from pydantic import BaseModel

class Publisher(BaseModel):
    id = int
    company_name = str
    book_id = int

    # Optional
    country = str