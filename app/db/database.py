from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB info from settings
from config.settings import settings

# DB URL
SQLALCHEMY_DATABASE_URL = settings.POSTGRES_URL 

# DB ENGINE
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# DB SESSION
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# DB BASE
Base = declarative_base()

#Gets the Database DONT DELETE
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()