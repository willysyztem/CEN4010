from models.base import Base
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

class ShoppingCart(Base):
    __tablename__ = __name__.lower()

    # books = relationship('Book', back_populates='wish_list')
    user = relationship('User', back_populates='shopping_cart')
    user_id = Column(Integer, ForeignKey('users.id'), ondelete='CASCADE', nullable=False)
    books = relationship('Books', back_populates='shoppingcart')
    books_id = Column(Integer, ForeignKey('books.id'))