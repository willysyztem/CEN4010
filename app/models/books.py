from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Integer, Date, Float
from sqlalchemy.orm import relationship
    
class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    isbn =  Column(String, unique = True, nullable = False)
    title = Column(String, nullable = False)
    published_date = Column(Date, nullable = False)
    description = Column(String)
    price = Column(Float, nullable = False)
    copies_sold = Column(Integer, nullable = False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable = False)
    publisher_id = Column(Integer, ForeignKey('publishers.id'), nullable = False)
    genre = Column(String)
    pages = Column(String)

    # Relationships
    author = relationship('Authors', back_populates='books')
    publisher = relationship('Publishers', back_populates='books')
    wishitems = relationship('WishItems', back_populates='book')
    cartitems = relationship('CartItems', back_populates='book')