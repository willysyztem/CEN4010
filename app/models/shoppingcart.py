from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

class shoppingcart(Base):
    __tablename__ = 'shoppingcart'

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)
    
    # Relationships
    owner = relationship('Users', back_populates='shoppingcart')
    cartitems = relationship('CartItems', back_populates='shoppingcart')
