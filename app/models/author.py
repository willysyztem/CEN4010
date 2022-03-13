# DB MODELS
from models.base import Base
from sqlalchemy import Column, Integer, String, Integer, Date, Float
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    biography = Column(String)

    books = relationship('books', back_populates='author')
    publisher_id =relationship('publisher', back_populates='author')