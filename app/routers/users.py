from turtle import update
from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models.users as models, schemas.users as schemas
import utils, oauth2

router = APIRouter(
    prefix = '/api/users',
    tags=['Profile Management']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_users(user: schemas.User, db: Session = Depends(get_db)): 
    try:
        #hash the password
        hashed_password = utils.hash(user.password)

        new_user = models.User(
            email = user.email,
            password = hashed_password,
            username = user.email,
            name = user.name,
            home_address = user.home_address
        )  
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='User already exists')

@router.get('/',  response_model=List[schemas.ShowUser])
def get_all_users(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find users')
    return users

@router.get('/{username}', response_model=schemas.ShowUser)
def get_user(username, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with username: {username}')
    return user

@router.put('/{username}', status_code=status.HTTP_202_ACCEPTED)
def update_user(username, user: schemas.User, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    updated_user = db.query(models.User).filter(models.User.username == username).update({
        'password': user.password,
        'name': user.name,
        'home_address': user.home_address
    })
    if not updated_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with username: {username}')
    db.commit()
    return {'detail': f'Update user {username}'}

@router.delete('/')
def delete_user(username, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status.HTTP_204_NO_CONTENT, f'No query found with username: {username}')
    db.delete(user)
    db.commit()
    return {'detail': f'Deleted user {username}'}