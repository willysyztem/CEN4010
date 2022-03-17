# DB MODELS
from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Integer, Date, Float
from sqlalchemy.orm import relationship
    
class cartItem(Base):
    __tablename__ = __name__.lower()

    id = Column(Integer, unique = True, nullable = False, primary_key = True)
    shoppingcart_id = Column(Integer, ForeignKey('shoppingcart.id', ondelete='CASCADE'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    book_title = Column(String, ForeignKey('books.title'), nullable=False)

    shoppingcart = relationship('shoppingcart', back_populates='cartItem')
    books = relationship('books', back_populates='cartItem')