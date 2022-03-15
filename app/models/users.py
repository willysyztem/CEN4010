from models.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = __name__.lower()

    id = Column(Integer, primary_key = True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True)
    name = Column(String)
    home_address = Column(String)

    # Relationships
    shoppingcart = relationship('ShoppingCart', back_populates='user')
    creditcards = relationship('CreditCards', back_populates='user')
    wishlist = relationship('WishList', back_populates='user')