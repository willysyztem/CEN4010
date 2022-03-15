from pydantic import BaseModel

class Publishers(BaseModel):
    id = int
    company_name = str
    book_id = int

    # Optional
    country = str