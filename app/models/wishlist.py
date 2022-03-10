from models.base import Base
from sqlalchemy import Column, ForeignKey,  Integer, String
from sqlalchemy.orm import relationship

class WishList(Base):
    __tablename__ = 'wish_list'

    id = Column(Integer, primary_key = True, index=True)
    name = Column(String, nullable=False, unique=True)
    books = Column(String)

    owner_username = Column(String, ForeignKey('users.username', ondelete='CASCADE'), nullable=False)
    owner = relationship('User', back_populates='wish_list', )