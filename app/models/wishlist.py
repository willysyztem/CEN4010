from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class WishList(Base):
    __tablename__ = 'wishlist'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    
    # Relationships
    owner = relationship('Users', back_populates='wishlist')
    wishitems = relationship('WishItems', back_populates='wishlist')