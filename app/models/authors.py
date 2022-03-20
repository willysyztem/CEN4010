# DB MODELS
from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Integer, Date, Float

class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    biography = Column(String)
    