from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db

import models.publishers as model
import schemas.publishers as schema

router = APIRouter(
    prefix = '/api/publishers',
    tags = ['Publishers']
)

@router.post('/', status_code = status.HTTP_201_CREATED, response_model = schema.Publishers)
def create_publisher(publisher: schema.Publishers, db: Session = Depends(get_db)):
    try:
        new_publisher = model.Publishers(
            id = len(db.query(model.Publishers).all()) +1,
            company_name = publisher.company_name,
            country = publisher.country
        )
        db.add(new_publisher)
        db.commit()
        db.refresh(new_publisher)
        return new_publisher
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'Publisher already exists')

@router.get('/')
def get_all_publishers(db: Session = Depends(get_db)):
    publishers = db.query(model.Publishers).all()
    if not publishers:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find publishers')
    return publishers

@router.get('/{publisher_id}', response_model = schema.Publishers)
def get_publisher(publisher_id, db: Session = Depends(get_db)):
    publisher = db.query(model.Publishers).filter(model.Publishers.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with publisher_id: {publisher_id}')
    return publisher

@router.put('/{publisher_id}', status_code = status.HTTP_202_ACCEPTED)
def update_publisher(publisher_id, publisher: schema.Publishers, db: Session = Depends(get_db)):
    publisher = db.query(model.Publishers).filter(model.Publishers.id == publisher_id).update({
        'company_name': publisher.company_name,
        'country': publisher.country
    })
    if not publisher:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with publisher_id: {publisher_id}')
    db.commit()
    return {'detail': f'Update publisher {publisher_id}'}

@router.delete('/')
def delete_publisher(publisher_id, db: Session = Depends(get_db)):
    publisher = db.query(model.Publishers).filter(model.Publishers.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status.HTTP_204_NO_CONTENT, f'No query found with publisher_id: {publisher_id}')
    db.delete(publisher)
    db.commit()
    return {'detail': f'Deleted publisher {publisher_id}'}