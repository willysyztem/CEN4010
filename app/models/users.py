from models.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True)
    name = Column(String)
    home_address = Column(String)

    shopping_cart = relationship('Shoppingcart', back_populates='user')

    credit_cards = relationship('CreditCard', back_populates='owner')
    wish_list = relationship('WishList', back_populates='owner')