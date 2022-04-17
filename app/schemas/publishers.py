from typing import Optional
from pydantic import BaseModel

# Publisher Schema
class Publishers(BaseModel):
    company_name : str
    country : Optional[str]