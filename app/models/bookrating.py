from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

class BookRating(Base):
    __tablename__ = 'book_ratings'

    id = Column(Integer, primary_key = True, index=True)
    book = Column(String, nullable=False, unique=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False)

class BookComment(Base):
    __tablename__ = 'book_comments'

    id = Column(Integer, primary_key = True, index=True)
    book = Column(String, nullable=False,)
    comment = Column(String, nullable=False)
    
    created_at = Column(Date, nullable=False)