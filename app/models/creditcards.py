from models.base import Base
from sqlalchemy import Column, ForeignKey,  Integer, String
from sqlalchemy.orm import relationship


class CreditCards(Base):
    __tablename__ = 'creditcards'

    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String, nullable=False, unique=True)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    # Relationships
    owner = relationship('Users', back_populates='creditcards')