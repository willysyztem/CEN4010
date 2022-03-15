from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models.wishlist as model
import schemas.wishlist as schema

import utils, oauth2

MAX_ALLOWED_WISHLIST = 3

router = APIRouter(
    prefix = '/api/wishlist',
    tags=['Wish List Management']
)

@router.post('/{user_id}')
def create_wish_list(user_id, new_wish_list: schema.WishList, db: Session = Depends(get_db)):
    existing_wishlist = db.query(model.WishList).filter(model.WishList.user_id == user_id).all()
    if len(existing_wishlist) < MAX_ALLOWED_WISHLIST:
            wish_list = model.WishList(
                name = new_wish_list.name,
                books = new_wish_list.books,
                user_id = user_id
            )
            for wishlist in existing_wishlist:
                if wishlist.name == wish_list.name:
                    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Wishlist name already exists => {wish_list.name}')
            db.add(wish_list)
            db.commit()
            db.refresh(wish_list)
            return {'detail': f'Wish List created for user with id: {wish_list.user_id}'}
    else:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Could not create wish list => Wishlist limit reached!')

@router.get('/{user_id}', response_model=List[schema.ShowWishList])
def get_wish_list(user_id, db: Session = Depends(get_db)):
    wish_list = db.query(model.WishList).filter(model.WishList.user_id == user_id).all()
    if not wish_list:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Could not find wishlist that belongs to user with id: {user_id}')
    return wish_list