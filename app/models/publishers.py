from models.base import Base
from sqlalchemy import Column, Integer, String, Integer
from sqlalchemy.orm import relationship

class Publishers(Base):
    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False, unique=True)
    country = Column(String)
    
    # Relationships
    books = relationship('Books', back_populates='publisher')