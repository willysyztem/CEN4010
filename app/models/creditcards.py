# DB MODELS
from models.base import Base
from sqlalchemy import Column, ForeignKey,  Integer, String
from sqlalchemy.orm import relationship


class CreditCard(Base):
    __tablename__ = 'credit_cards'

    id = Column(Integer, primary_key = True, index=True)
    card_number = Column(String, nullable=False, unique=True)

    owner_username = Column(String, ForeignKey('users.username', ondelete='CASCADE'), nullable=False)
    owner = relationship('User', back_populates='credit_cards')