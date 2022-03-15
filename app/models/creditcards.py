# DB MODELS
from models.base import Base
from sqlalchemy import Column, ForeignKey,  Integer, String
from sqlalchemy.orm import relationship


class CreditCards(Base):
    __tablename__ = __name__.lower()

    id = Column(Integer, primary_key = True, index=True)
    card_number = Column(String, nullable=False, unique=True)

    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', back_populates='creditcards')