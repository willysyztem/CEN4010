from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models.wishlist as model
import models.wishitems
import models.cartitems

import schemas.wishlist as schema

from routers.shoppingcart import add_cartitem
from routers.books import get_book_by_id


MAX_ALLOWED_WISHLIST = 3

router = APIRouter(
    prefix = '/api/wishlist',
    tags = ['Wish List Management']
)

@router.post('/{user_id}', status_code = status.HTTP_201_CREATED)
def create_wishlist(user_id: int, new_wishlist: schema.WishList, db: Session = Depends(get_db)):
    existing_wishlist = db.query(model.WishList).filter(model.WishList.owner_id == user_id).all()
    if len(existing_wishlist) < MAX_ALLOWED_WISHLIST:
            wish_list = model.WishList(
                name = new_wishlist.name,
                owner_id = user_id
            )
            for wishlist in existing_wishlist:
                if wishlist.name == wish_list.name:
                    raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Wishlist name already exists => {wish_list.name}')
            db.add(wish_list)
            db.commit()
            db.refresh(wish_list)
            return {'detail': f'Wish List created for user with id: {user_id}'}
    else:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Could not create wish list => Wishlist limit reached!')

@router.get('/{user_id}')
def get_wishlist(user_id: int, db: Session = Depends(get_db)):
    wishlists = db.query(model.WishList).filter(model.WishList.owner_id == user_id).all()
    for wishlist in wishlists:
        wishlist.wishitems = get_all_wishitems_from_wishlist(wishlist.id, db)
    if not wishlists:
        return {}
    return wishlists

@router.delete('/{wishlist_id}')
def delete_wishlist(wishlist_id, db: Session = Depends(get_db)):
    try:
        wishlist = db.query(model.WishList).filter(model.WishList.id == wishlist_id).first()
        if not wishlist:
            raise HTTPException(status.HTTP_204_NO_CONTENT, f'No wishlist with id : {wishlist_id}')
        db.delete(wishlist)
        db.commit()
        return {'detail': f'Deleted wishlist {wishlist_id}'}
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Could not delete wishlist => {e}')

# WishItems
@router.post('/wishitems/', status_code = status.HTTP_201_CREATED)
def add_wishitem(new_wishitem: schema.WishItem, db: Session = Depends(get_db)):
    try:
        wishitem = models.wishitems.WishItems(
            wishlist_id = new_wishitem.wishlist_id,
            book_id = new_wishitem.book_id,
        )
        db.add(wishitem)
        db.commit()
        db.refresh(wishitem)
        return {'detail': f'Cart item created for wishlist with id: {wishitem.wishlist_id}'}
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Could not create cart item.')

# @router.delete('/wishitems/{wishitem_id}')
# def delete_wishitem(wishitem_id, db: Session = Depends(get_db)):
#     wishitem = db.query(models.cartitems.CartItems).filter(models.cartitems.CartItems.id == wishitem_id).first()
#     if not wishitem:
#         raise HTTPException(status.HTTP_204_NO_CONTENT, f'No wishitem with id : {wishitem_id}')
#     db.delete(wishitem)
#     db.commit()
#     return {'detail': f'Deleted wishitem {wishitem_id}'}

@router.get('/wishitems/{wishlist_id}')
def get_all_wishitems_from_wishlist(wishlist_id: int, db: Session = Depends(get_db)):
    wishitems = db.query(models.wishitems.WishItems).filter(models.wishitems.WishItems.wishlist_id == wishlist_id).all()
    for wishitem in wishitems:
        wishitem.book = get_book_by_id(wishitem.book_id, db)
    if not wishitems:
        return []
    return wishitems

@router.get('/wishitem/{wishitem_id}', )
def get_wishitem(wishitem_id: int, db: Session = Depends(get_db)):
    wishitem = db.query(models.wishitems.WishItems).filter(models.wishitems.WishItems.id == wishitem_id).first()
    wishitem.book = get_book_by_id(wishitem.book_id, db)
    if not wishitem:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Could not find cart item that belongs to wishlist with id: {wishitem_id}')
    return wishitem

@router.post('/wishitem/{wishitem_id}&&{user_id}', status_code = status.HTTP_201_CREATED)
def add_wishitem_to_shoppingcart(wishitem_id: int, user_id: int, db: Session = Depends(get_db)):
    try:
        wishitem = get_wishitem(wishitem_id, db)
        new_cartitem = add_cartitem(user_id, models.cartitems.CartItems(book_id=wishitem.book_id), db)
        db.add(new_cartitem)
        db.commit()
        db.refresh(new_cartitem)
        return new_cartitem
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Could not add wishitem to cart item => {e}')