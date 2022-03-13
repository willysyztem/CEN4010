from models.base import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

class Shoppingcart(Base):
    __tablename__ = __name__.lower()

    # books = relationship('Book', back_populates='wish_list')
    username = Column(String, ForeignKey('users.username', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), ondelete='CASCADE', nullable=False)
    books = relationship('Books', back_populates='shoppingcart')
    books_id = Column(Integer, ForeignKey('books.id'))