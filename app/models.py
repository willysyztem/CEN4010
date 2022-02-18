# DB MODELS
from db.database import Base
from sqlalchemy import Column, ForeignKey,  Integer, String, DateTime
from sqlalchemy.orm import relationship

# CREATE MODELS UNDER HERE
# 
# USER MODEL
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True)
    name = Column(String)
    home_address = Column(String)

    credit_cards = relationship('CreditCard', back_populates='owner')

    # created_at = Column()

class CreditCard(Base):
    __tablename__ = 'credit_cards'

    id = Column(Integer, primary_key = True, index=True)
    card_number = Column(String, nullable=False, unique=True)

    owner_username = Column(String, ForeignKey('users.username'))
    owner = relationship('User', back_populates='credit_cards')

    # created_at = Column()