from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db

import models.creditcards as models, schemas.creditcards as schemas
import utils, oauth2

router = APIRouter(
    prefix = '/api/creditcard',
    tags=['Credit Cards']
)

@router.post('/{username}', status_code=status.HTTP_201_CREATED)
def create_credit_card(username, credit_card: schemas.CreditCard, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    new_credit_card = models.CreditCard(
        card_number = credit_card.card_number,
        owner_username = credit_card.owner_username
    )
    try:
        db.add(new_credit_card)
        db.commit()
        db.refresh(new_credit_card)
        return {'detail': f'Credit Card created for {username}'}
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='User already exists')

@router.get('/{username}')
def get_user_credit_cards(username, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    credit_cards = db.query(models.CreditCard).filter(models.CreditCard.owner_username == username)
    if not credit_cards:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No credit cards found with username: {username}')
    return credit_cards