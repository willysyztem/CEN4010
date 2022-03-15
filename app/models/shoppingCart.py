from turtle import back
from app.models.cartItem import cartItem
from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class ShoppingCart(Base):
    __tablename__ = __name__.lower()

    id = Column(Integer, primary_key = True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    cart_item_id = Column(Integer, ForeignKey('cartItem.id'))
    
    user = relationship('User', back_populates='ShoppingCart')
    cartItem = relationship('cartItem', back_populates='ShoppingCart')