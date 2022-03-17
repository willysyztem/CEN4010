from turtle import back
from app.models.cartItem import cartItem
from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class ShoppingCart(Base):
    __tablename__ = 'shoppingcart'

    id = Column(Integer, primary_key = True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    cart_item_id = Column(Integer, ForeignKey('cartItem.id'))
    
    user = relationship('User', back_populates='ShoppingCart')
    cartItem = relationship('cartItem', back_populates='ShoppingCart')

    def to_json(self):
        return {
            "id":self.id,
            "user_id":self.user_id,
            "cart_item_id":self.cart_item_id,
            "user":self.user,
            "cartItem": self.cartItem
        }