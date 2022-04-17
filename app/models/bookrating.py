from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

class BookRating(Base):
    __tablename__ = 'book_ratings'

    id = Column(Integer, primary_key = True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    book = Column(String, ForeignKey('books.isbn', ondelete='CASCADE'), nullable=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

class BookComment(Base):
    __tablename__ = 'book_comments'

    id = Column(Integer, primary_key = True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    book = Column(String, ForeignKey('books.isbn', ondelete='CASCADE'), nullable=False)
    comment = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)