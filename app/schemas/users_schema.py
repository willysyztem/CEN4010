from ctypes import Array
from numbers import Number
from typing import Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy import Integer, Date

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
    publishedDate = Date
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
    
class PublisherSchema(BaseModel):
    publisher_id = Integer
    book_id = Integer

    # Optional
    country = str

class OrderSchema(BaseModel):
    order_id = Integer
    user_id = Integer
    orderDate = Date
    subtotal = Number
    shipping = Number
    total = subtotal + shipping
