# DB MODELS
from models.base import Base
from sqlalchemy import Column, ForeignKey,  Integer, String
from sqlalchemy.orm import relationship


class CreditCards(Base):
    __tablename__ = 'creditcards'

    id = Column(Integer, primary_key = True, index=True)
    card_number = Column(String, nullable=False, unique=True)

    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', back_populates='creditcards')

    def to_json(self):
        return {
            "id":self.id,
            "card_number":self.card_number,
            "user_id":self.user_id,
            "user":self.user
        }