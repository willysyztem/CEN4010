# DB MODELS
from db.database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey,  Integer, String, null, text, BigInteger
from sqlalchemy.orm import relationship

# CREATE MODELS UNDER HERE
# 
# USER MODEL
class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key = True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True)
    name = Column(String)
    home_address = Column(String)

    credit_cards = relationship('CreditCard', back_populates='owner')
    wish_list = relationship('WishList', back_populates='owner')

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class CreditCard(Base):
    __tablename__ = 'credit_cards'

    id = Column(BigInteger, primary_key = True, index=True)
    card_number = Column(String, nullable=False, unique=True)

    owner_username = Column(String, ForeignKey('users.username', ondelete='CASCADE'), nullable=False)
    owner = relationship('User', back_populates='credit_cards')

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class WishList(Base):
    __tablename__ = 'wish_list'

    id = Column(BigInteger, primary_key = True, index=True)
    name = Column(String, nullable=False, unique=True)
    books = Column(String)

    owner_username = Column(String, ForeignKey('users.username', ondelete='CASCADE'), nullable=False)
    owner = relationship('User', back_populates='wish_list', )

    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))