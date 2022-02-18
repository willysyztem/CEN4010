from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

from jose import JWSError, jwt 
from datetime import datetime, timedelta

import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

#SECRET_KEY
#ALGO 
#EXPIRATION

# openssl rand -hex 32
SECRET_KEY = '19af20df8a8d2025532e3ad86df08a7565a13f3f17644f84d874004a4ca741db'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_econde = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_econde.update({"exp": expire})

    encoded_jwt = jwt.encode(to_econde, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, [ALGORITHM])
        
        id: str = payload.get('user_id')
        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWSError:
        raise credentials_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Could not validate login', headers={'WWW-Authenticate': 'Bearer'})
    return verify_access_token(token, credentials_exception )