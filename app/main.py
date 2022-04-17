from fastapi import FastAPI, responses
from fastapi.staticfiles import StaticFiles

# Settings For Fast API & DB
from config.settings import settings

# DB
from db.database import engine

# The code blows creates the tables from models
from models.base import Base
Base.metadata.create_all(bind=engine)

# Import base router (carries all the other routers)
from routers import base


#Boilerplate stuff for fastapi
def start_app():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        version=settings.PROJECT_VERSION
    )
    app.include_router(base.main_router)

    # mount static files
    app.mount('/static', StaticFiles(directory='static'), name='static')
    
    return app

app = start_app()

@app.get('/', include_in_schema=False)
def redirect():
    return responses.RedirectResponse('/login')