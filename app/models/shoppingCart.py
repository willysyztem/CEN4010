from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class ShoppingCart(Base):
    __tablename__ = 'shoppingcart'

    id = Column(Integer, primary_key = True, index=True)

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', back_populates='shoppingcart', )