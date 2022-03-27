from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db

import models.creditcards as model
import schemas.creditcards as schema

import utils, oauth2

router = APIRouter(
    prefix = '/api/creditcard',
    tags = ['Credit Cards']
)

@router.post('/{user_id}', status_code = status.HTTP_201_CREATED)
def create_creditcard(id, creditcard : schema.CreditCard, db: Session = Depends(get_db)):
    new_creditcard = model.CreditCards(
        card_number = creditcard.card_number,
        user_id = id
    )
    try:
        db.add(new_creditcard)
        db.commit()
        db.refresh(new_creditcard)
        return {'detail': f'Credit Card created for user with id: {id}'}
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'User already exists')

@router.get('/{user_id}')
def get_user_creditcards(user_id, db: Session = Depends(get_db)):
    creditcards = db.query(model.CreditCards).filter(model.CreditCards.user_id == user_id).all()
    if not creditcards:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No credit cards found with user id: {user_id}')
    return creditcards