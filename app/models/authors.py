# DB MODELS
from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Integer, Date, Float
from sqlalchemy.orm import relationship

class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    biography = Column(String)
    publisher_id = Column(Integer, ForeignKey('publisher.id'), nullable=True)

    publisher = relationship('publisher', back_populates='author')