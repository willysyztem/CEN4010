# DB MODELS
from ctypes import Array
from numbers import Number

from h11 import Data
from db.database import Base
from sqlalchemy import Column, Integer, String, null

# CREATE MODELS UNDER HERE
# 
# USER MODEL
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index=True)
    email_address = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True)

    # Optional
    name = Column(String)
    home_address = Column(String)

    def __repr__(self):
        return f"<User(username={self.username})>"

# BOOK MODEL
class Book(Base):
    __tablename__ = 'books'

    isbn =  Column(String, unique = True, nullable = False, primary_key = True)
    title = Column(String, nullable = False)
    author_id = Column(Integer, nullable = False)
    publisher = Column(String, nullable = False)
    publishedDate = Column(Data, nullable = False)
    description = Column(String)
    price = Column(Number, nullable = False)
    copiesSold = Column(Integer, nullable = False)

# AUTHOR MODEL
class Author(Base):
    __tablename__='authors'

    author_id = Column(Integer, nullable=False, unique=True, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    publisher = Column(String)
    biography = Column(String)
    books = Column(Array)
