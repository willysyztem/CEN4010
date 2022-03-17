from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models.cartItem as model
import schemas.cartItem as schema

import utils
import oauth2

MAX_ALLOWED_WISHLIST = 3

router = APIRouter(
    prefix='/api/cartItem',
    tags=['CartItem']
)


@router.post('/{cart_id}')
def create_cart_item(cart_id, new_cart_item: schema.cartItem, db: Session = Depends(get_db)):
    try:
        cart_item = model.cartItem(
            id=new_cart_item.id,
            shoppingcart_id=new_cart_item.shoppingcart_id,
            title=new_cart_item.book_title,
            book_id=new_cart_item.book_id,
        )
        db.add(cart_item)
        db.commit()
        db.refresh(cart_item)
        return {'detail': f'Cart item created for shoppingCart with id: {cart_id}'}
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f'Could not create cart item.')


@router.get('/{cart_id}', response_model=List[schema.cartItem])
def get_cart_items(cart_id, db: Session = Depends(get_db)):
    cart_items = db.query(model.cartItem).filter(
        model.cartItem.shoppingcart_id == cart_id).all()
    if not cart_items:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail=f'Could not find cart items that belongs to user with cart id: {cart_id}')
    return cart_items
