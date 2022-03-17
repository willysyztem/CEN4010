from pydantic import BaseModel

class Publishers(BaseModel):
    id = int
    company_name = str

    # Optional
    country = str