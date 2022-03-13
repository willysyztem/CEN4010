from fastapi import FastAPI

# Settings For Fast API & DB
from config.settings import settings

# DB
from db.database import engine

# The code blows creates the tables from models
from models.base import Base
Base.metadata.create_all(bind=engine)

# Import all routers (apis)
from routers import auth, creditcards, users, wishlist, books, author, order, publisher, shoppingcart


#Boilerplate stuff for fastapi
def start_app():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        version=settings.PROJECT_VERSION
    )
    app.include_router(auth.router)
    app.include_router(creditcards.router)
    app.include_router(users.router)
    app.include_router(wishlist.router)
    app.include_router(books.router)
    app.include_router(authors.router)
    app.include_router(order.router)
    app.include_router(publisher.router)
    app.include_router(shoppingcart.router)
    return app

app = start_app()