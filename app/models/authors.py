from models.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    biography = Column(String)

    # Relationships
    books = relationship('Books', back_populates='author')