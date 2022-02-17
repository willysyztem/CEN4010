# DB MODELS
from ctypes import Array
from numbers import Number

from db.database import Base
from sqlalchemy import Column, Date, Integer, String

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

    book_id = Column(Integer, unique = True, nullable = False, primary_key = True)
    isbn =  Column(String, unique = True, nullable = False)
    title = Column(String, nullable = False)
    author_id = Column(Integer, nullable = False)
    publisher = Column(String, nullable = False)
    publishedDate = Column(Date, nullable = False)
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

# PUBLISHER MODEL
class Publisher(Base):
    __tablename__='publishers'

    publisher_id = Column(Integer, nullable=False, unique=True, primary_key=True, index=True)
    book_id = Column(Integer, unique = True, nullable = False, primary_key=True)
    country = Column(String)

# ORDERS
class Orders(Base):
    __tablename__='orders'

    order_id = Column(Integer, unique = True, nullable = False, primary_key=True, index=True)
    user_id = Column(Integer, unique = True, nullable = False, primary_key=True)
    orderDate = Column(Date, nullable=False)
    subtotal = Column(Number, nullable=False)
    shipping = Column(Number, nullable=False)
    