from app.routers.vote import vote
from fastapi import FastAPI

# Settings For Fast API & DB
from config.settings import settings

# DB
from db.database import engine

# The code blows creates the tables from models
from models import Base
Base.metadata.create_all(bind=engine)

# Import all routers (apis)
from routers import auth, credit_cards, users, wishlist, vote


#Boilerplate stuff for fastapi
def start_app():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        version=settings.PROJECT_VERSION
    )
    app.include_router(auth.router)
    app.include_router(credit_cards.router)
    app.include_router(users.router)
    app.include_router(wishlist.router)
    app.include_router(vote.router)
    return app

app = start_app()