from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, Integer
from sqlalchemy.orm import relationship
    
class CartItems(Base):
    __tablename__ = 'cartitems'

    id = Column(Integer, primary_key=True, index=True)
    shoppingcart_id = Column(Integer, ForeignKey('shoppingcart.id', ondelete='CASCADE'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    book = relationship('Books', back_populates='cartitems')
    shoppingcart = relationship('ShoppingCart', back_populates='cartitems')