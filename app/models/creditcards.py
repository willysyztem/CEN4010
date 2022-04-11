from enum import unique
from models.base import Base
from sqlalchemy import Column, ForeignKey,  Integer, String
from sqlalchemy.orm import relationship


class CreditCards(Base):
    __tablename__ = 'creditcards'

    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)

    # Relationships
    owner = relationship('Users', back_populates='creditcards')