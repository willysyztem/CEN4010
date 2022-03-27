from typing import Optional
from pydantic import BaseModel

# Author Schema
class Authors(BaseModel):
    first_name : str
    last_name : str
    biography : Optional[str]