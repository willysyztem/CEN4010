# DB MODELS
from models.base import Base
from sqlalchemy import Column, Integer, String, Integer, Date, Float
from sqlalchemy.orm import relationship
    
class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, unique = True, nullable = False, primary_key = True)
    isbn =  Column(String, unique = True, nullable = False)
    title = Column(String, nullable = False)
    author_id = Column(Integer, nullable = False)
    publisher = Column(String, nullable = False)
    publishedDate = Column(Date, nullable = False)
    description = Column(String)
    price = Column(Float, nullable = False)
    copiesSold = Column(Integer, nullable = False)

    shoppingcart = relationship('shoppingcart', back_populates='books')