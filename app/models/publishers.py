# DB MODELS
from models.base import Base
from sqlalchemy import Column, Integer, String, Integer, Date, Float
from sqlalchemy.orm import relationship

class Publishers(Base):
    __tablename__ = 'publishers'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    country = Column(String)

    
    book_id = relationship('books', back_populates='publisher')