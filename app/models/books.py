# DB MODELS
from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Integer, Date, Float
from sqlalchemy.orm import relationship
    
class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, unique = True, nullable = False, primary_key = True)
    isbn =  Column(String, unique = True, nullable = False)
    title = Column(String, nullable = False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable = False)
    publisher_id = Column(Integer, ForeignKey('publishers.id'), nullable = False)
    publishedDate = Column(Date, nullable = False)
    description = Column(String)
    price = Column(Float, nullable = False)
    copiesSold = Column(Integer, nullable = False)
    genre = Column(String, nullable = False)
    rating = Column(Integer, nullable = False)

    author = relationship('author', back_populates='books')