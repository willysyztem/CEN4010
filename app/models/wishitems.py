from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, Integer
from sqlalchemy.orm import relationship
    
class WishItems(Base):
    __tablename__ = 'wishitems'

    id = Column(Integer, primary_key=True, index=True)
    wishlist_id = Column(Integer, ForeignKey('wishlist.id', ondelete='CASCADE'), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    wishlist = relationship('WishList', back_populates='wishitems')
    book = relationship('Books', back_populates='wishitems')