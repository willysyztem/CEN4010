# DB MODELS
from db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# CREATE MODELS UNDER HERE
# 
# USER MODEL
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index=True)
    email_address = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True)

    # Optional
    name = Column(String)
    home_address = Column(String)
    credit_cards = relationship('Credit_Card', back_populates='owner')

    def __repr__(self):
        return f'<User(username={self.username})>'

# CREDIT CARD MODEL
class Credit_Card(Base):
    __tablename__ = 'credit_card'

    id = Column(Integer, primary_key = True, index=True)
    card_number = Column(String, nullable=False)
    expiration_date = Column(String, nullable=False)
    ccv = Column(String, nullable=False)
    card_name = Column(String, nullable=False)
    owner = relationship('User', back_populates='credit_cards')
    user_id = Column(Integer, ForeignKey('users.id'))