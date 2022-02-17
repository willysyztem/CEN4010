# DB MODELS
from db.database import Base
from sqlalchemy import Column,  Integer, String

# CREATE MODELS UNDER HERE
# 
# USER MODEL
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True)
    name = Column(String)
    home_address = Column(String)

    def __repr__(self):
        return f'<User(username={self.username})>'