from datetime import timedelta
from typing import Callable, Optional, Iterator, Callable

from fastapi import Depends, status, APIRouter
from fastapi.responses import RedirectResponse
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

SECRET_KEY = '19af20df8a8d2025532e3ad86df08a7565a13f3f17644f84d874004a4ca741db'

manager = LoginManager(
    secret=SECRET_KEY, 
    token_url='/login', 
    use_cookie=True, 
    cookie_name='login-bs.cookie',
    default_expiry=timedelta(hours=12)
    )

from sqlalchemy.orm import Session
from db.database import get_db

from models.users import Users

import utils

router = APIRouter(tags=['Authentication'])

@manager.user_loader(session_provider=get_db)
def get_user_by_username(
    _username: str, 
    db: Optional[Session] = None,
    session_provider: Callable[[], 
    Iterator[Session]] = None
):
    if db is None and session_provider is None:
        raise ValueError("db and session_provider cannot both be None.")

    if db is None:
        db = next(session_provider())

    user = db.query(Users).where(Users.username == _username).first()
    return user

@router.post('/login')
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    username = data.username
    password = data.password
    user = get_user_by_username(username, db)
    if not user:
        raise InvalidCredentialsException
    # verifies if login password is the same
    verified = utils.verify(password, user.password)
    if not verified:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data = {'sub': username}
    )
    response = RedirectResponse(url='/index', status_code=status.HTTP_302_FOUND)
    manager.set_cookie(response, access_token)
    return response