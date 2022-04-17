from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db

import models.creditcards as model
import schemas.creditcards as schema

router = APIRouter(
    prefix = '/api/creditcard',
    tags = ['Credit Cards']
)
  
@router.post('/{user_id}', status_code = status.HTTP_201_CREATED)
def create_creditcard(user_id, creditcard: schema.CreditCard, db: Session = Depends(get_db)):
    new_creditcard = model.CreditCards(
        card_number = creditcard.card_number,
        owner_id = user_id
    )
    try:
        db.add(new_creditcard)
        db.commit()
        db.refresh(new_creditcard)
        return {'detail': f'Credit Card created'}
    except Exception:
        return HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'User Already has a credit card entry')

@router.get('/{user_id}')
def get_user_creditcards(user_id, db: Session = Depends(get_db)):
    creditcards = db.query(model.CreditCards).filter(model.CreditCards.owner_id == user_id).first()
    if not creditcards:
        return HTTPException(status.HTTP_404_NOT_FOUND, detail = f'No creditcard found for user with id {user_id}')
    return creditcards

@router.put('/{user_id}')
def update_user_creditcard(user_id, creditcard: schema.CreditCard, db: Session = Depends(get_db)):
    updated_cc = db.query(model.CreditCards).filter(model.CreditCards.owner_id == user_id).update({
        'card_number' : creditcard.card_number
    })
    if not updated_cc:
        return HTTPException(status.HTTP_404_NOT_FOUND, detail = f'No query found with id: {user_id}')
    db.commit()
    return {'detail': f'Updated user credit card'}