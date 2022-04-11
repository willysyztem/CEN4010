from fastapi import Depends, status, HTTPException, APIRouter
from typing import List
from pydantic import EmailStr

from sqlalchemy.orm import Session
from db.database import get_db

import models.users as model
import schemas.users as schema

from routers.shoppingcart import create_shoppingcart

import utils

router = APIRouter(
    prefix = '/api/users',
    tags = ['Profile Management']
)

# current_user_id: int = Depends(oauth2.get_current_user)

@router.post('/', status_code = status.HTTP_201_CREATED, response_model=schema.ShowUser)
def create_user(user: schema.User, db: Session = Depends(get_db)): 
    try:
        #hash the password
        hashed_password = utils.hash(user.password)

        new_user = model.Users(
            id = len(db.query(model.Users).all()) +1,
            email = user.email,
            password = hashed_password,
            username = user.email,
            name = user.name,
            home_address = user.home_address
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        # initiate shopping cart for user
        create_shoppingcart(new_user.id, db)
        return new_user
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'User already exists')

@router.get('/', response_model = List[schema.ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(model.Users).all()
    if not users:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find users')
    return users

# @router.get('/{username}', response_model = List[schema.ShowUser])
# def get_user(username: EmailStr, db: Session = Depends(get_db)):
#     user = db.query(model.Users).filter(model.Users.username == username).first()
#     if not user:
#         raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with username: {username}')
#     return user

@router.put('/{username}')
def update_user(username: EmailStr, user_info: schema.UpdateUser, db: Session = Depends(get_db)):
    updated_user = db.query(model.Users).filter(model.Users.username == username).update({
        'password': utils.hash(user_info.password),
        'name': user_info.name,
        'home_address': user_info.home_address
    })
    if not updated_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with username: {username}')
    db.commit()
    return {'detail': f'Update user {username}'}

@router.delete('/')
def delete_user(username: EmailStr, db: Session = Depends(get_db)):
    user = db.query(model.Users).filter(model.Users.username == username).first()
    if not user:
        raise HTTPException(status.HTTP_204_NO_CONTENT, f'No query found with username: {username}')
    db.delete(user)
    db.commit()
    return {'detail': f'Deleted user {username}'}