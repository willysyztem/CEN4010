from time import timezone
from models.base import Base
from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.orm import relationship

from datetime import date

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True)
    name = Column(String)
    home_address = Column(String)
    is_superuser = Column(Boolean, nullable=False, default=False)
    date_created = Column(Date, nullable=False, default=date.today())

    # Relationships
    order = relationship('Orders', back_populates='owner')
    shoppingcart = relationship('ShoppingCart', back_populates='owner')
    creditcards = relationship('CreditCards', back_populates='owner')
    wishlist = relationship('WishList', back_populates='owner')