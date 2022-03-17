from models.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'users'

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

    def to_json(self):
        return {
            "id":self.id,
            "email":self.email,
            "password":self.password,
            "username":self.username,
            "name": self.name,
            "home_address": self.home_address,
            "shoppingcart":self.shoppingcart,
            "creditcards": self.creditcards,
            "wishlist": self.wishlist
        }