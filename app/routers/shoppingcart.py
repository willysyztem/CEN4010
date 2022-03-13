from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models.shoppingcart as models, schemas.shoppingcart as cartSchema
import utils

router = APIRouter(
    prefix = '/api/shoppingcart',
    tags=['Shopping Cart Management']
)

@router.post('/{username}')
def create_shopping_cart(username, new_shopping_cart: cartSchema.ShoppingCart, db: Session = Depends(get_db)):
    try:
        shopping_cart = models.WishList(
            user = new_shopping_cart.user,
            books = new_shopping_cart.books
        )
        db.add(shopping_cart)
        db.commit()
        db.refresh(shopping_cart)
        return {'detail': f'Shopping Cart created for {shopping_cart.owner_username}'}
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'Could not create shopping cart => {e}')

@router.get('/{username}', response_model=List[cartSchema.ShowShoppingCart])
def get_shopping_cart(username, db: Session = Depends(get_db)):
    shopping_cart = db.query(models.Shoppingcart).filter(models.Shoppingcart.username == username).all()
    if not shopping_cart:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f'Could not find shopping cart that belongs to {username}')
    return shopping_cart