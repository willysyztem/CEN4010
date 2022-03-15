# DB MODELS
from models.base import Base
from sqlalchemy import Column, Integer, String, Integer, Date, Float
from sqlalchemy.orm import relationship

class Orders(Base):
    __tablename__ = __name__.lower()

    id = Column(Integer, unique=True, nullable=False, primary_key=True, index=True)
    orderDate = Column(Date, nullable=False)
    subtotal = Column(Integer, nullable=False)
    shipping = Column(Integer, nullable=False)

    
    user_id = relationship('users', back_populates='order')