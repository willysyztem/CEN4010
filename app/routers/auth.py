from fastapi import Depends, status, HTTPException, APIRouter, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from db.database import get_db

import models, schemas, utils, oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.username == user_login.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Login')
    # verifies if login password is the same
    verified = utils.verify(user_login.password, user.password)
    if not verified:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'Invalid Login')

    access_token = oauth2.create_access_token(data={'user_id': user.id})
    return {'access_token': access_token, "token_type": 'bearer'}