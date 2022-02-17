from ctypes import Array
from datetime import date
from numbers import Number
from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy import Integer

class UserSchema(BaseModel):
    email: EmailStr
    password: str

    # Optional Fields To Project Specs
    name: Optional[str]
    home_address: Optional[str]

class BookSchema(BaseModel):
    isbn =  str
    title = str
    author_id = Integer
    publisher = str
    publishedDate = date
    price = Number
    copiesSold = Integer

    # Optional
    description = str

class AuthorSchema(BaseModel):
    author_id = Integer
    firstName = str
    lastName = str
    fullName = lastName + ', ' + firstName

    # Optional
    publisher = str
    biography = str
    books = Array
    