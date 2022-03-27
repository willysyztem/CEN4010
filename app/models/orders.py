from models.base import Base
from sqlalchemy import Column, ForeignKey, Integer, Integer, Date
from sqlalchemy.orm import relationship

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    order_date = Column(Date, nullable=False)
    subtotal = Column(Integer, nullable=False)
    shipping = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    # Relationships
    owner = relationship('Users', back_populates='order')