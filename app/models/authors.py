# DB MODELS
from base import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

class Authors(Base):
    __tablename__ = 'authors'

    id = Column(Integer, nullable=False, unique=True, primary_key=True, index=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    biography = Column(String)
    publisher_id = Column(Integer, ForeignKey('publisher.id'), nullable=True)

    publisher = relationship('publisher', back_populates='author')

    def to_json(self):
        return {
            "id":self.id,
            "firstName":self.firstName,
            "lastName":self.lastName,
            "biography":self.biography,
            "publisher_id": self.publisher_id
        }