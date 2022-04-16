from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db

import models.shoppingCart as model
import models.cartitems

import schemas.shoppingcart as schema

import utils

router = APIRouter(
    prefix = '/api/shoppingcart',
    tags = ['Shopping Cart Management']
)

@router.post('/{user_id}')
def create_shoppingcart(user_id: int, db: Session = Depends(get_db)):
    try:
        new_shoppingcart = model.ShoppingCart(
            owner_id = user_id
        )
        db.add(new_shoppingcart)
        db.commit()
        db.refresh(new_shoppingcart)
        return new_shoppingcart
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Could not create shopping cart => {e}')

@router.get('/{user_id}')
def get_shoppingcart(user_id: int, db: Session = Depends(get_db)):
    shoppingcart = db.query(model.ShoppingCart).filter(model.ShoppingCart.owner_id == user_id).first()
    if not shoppingcart:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Could not find shopping cart that belongs to user with id: {user_id}')
    return shoppingcart

# CartItems
@router.post('/cartitems/{user_id}', status_code = status.HTTP_201_CREATED)
def add_cartitem(user_id: int, cartitems: schema.CartItem, db: Session = Depends(get_db)):
    try:
        shoppingcart = db.query(model.ShoppingCart).filter(model.ShoppingCart.owner_id == user_id).first()
        new_cartitems = models.cartitems.CartItems(
            shoppingcart_id = shoppingcart.id,
            book_id = cartitems.book_id
        )
        db.add(new_cartitems)
        db.commit()
        db.refresh(new_cartitems)
        return new_cartitems
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Could not create cart item.')

@router.get('/cartitems/{shoppingcart_id}')
def get_all_cartitems_from_shoppingcart(shoppingcart_id: int, db: Session = Depends(get_db)):
    cartitems = db.query(models.cartitems.CartItems).filter(models.cartitems.CartItems.shoppingcart_id == shoppingcart_id).all()
    if not cartitems:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Could not find cart items that belongs shoppingcart id: {shoppingcart_id}')
    return cartitems

@router.get('/cartitems/{cartitem_id}')
def get_cartitem(cartitem_id: int, db: Session = Depends(get_db)):
    cartitem = db.query(models.cartitems.CartItems).filter(models.cartitems.CartItems.id == cartitem_id).first()
    if not cartitem:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Could not find cart item with id: {cartitem_id}')
    return cartitem