from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models
import schemas

router = APIRouter(
    prefix='/api/publishers',
    tags=['Publishers']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Publisher)
def create_publisher(publisher: schemas.Publisher, db: Session = Depends(get_db)):
    try:
        new_publisher = models.Publisher(
            publisher_id=publisher.publisher_id,
            book_id=publisher.book_id,
            country=publisher.country
        )
        db.add(new_publisher)
        db.commit()
        db.refresh(new_publisher)
        return new_publisher
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail='publisher already exists')


@router.get('/',  response_model=List[schemas.Publisher])
def get_all_publishers(db: Session = Depends(get_db)):
    publishers = db.query(models.Publisher).all()
    if not publishers:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find publishers')
    return publishers


@router.get('/{publisher_id}', response_model=schemas.Publisher)
def get_publisher(publisher_id, db: Session = Depends(get_db)):
    publisher = db.query(models.Publisher).filter(models.Publisher.publisher_id == publisher_id).first()
    if not publisher:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with publisher_id: {publisher_id}')
    return publisher


@router.get('/{title}', response_model=schemas.Publisher)
def get_publisher(title, db: Session = Depends(get_db)):
    publisher = db.query(models.Publisher).filter(models.Publisher.publisher_id == title).first()
    if not publisher:
        raise HTTPException(status.HTTP_404_NOT_FOUND,'No query found with title: {title}')
    return publisher


@router.put('/{publisher_id}', status_code=status.HTTP_202_ACCEPTED)
def update_publisher(publisher_id, publisher: schemas.Publisher, db: Session = Depends(get_db)):
    publisher = db.query(models.Publisher).filter(models.Publisher.publisher_id == publisher_id).update({
        'book_id': publisher.book_id,
        'country': publisher.country
    })
    if not publisher:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with publisher_id: {publisher_id}')
    db.commit()
    return {'detail': f'Update publisher {publisher_id}'}


@router.delete('/')
def delete_publisher(publisher_id, db: Session = Depends(get_db)):
    publisher = db.query(models.Publisher).filter(models.Publisher.publisher_id == publisher_id).first()
    if not publisher:
        raise HTTPException(status.HTTP_204_NO_CONTENT, f'No query found with publisher_id: {publisher_id}')
    db.delete(publisher)
    db.commit()
    return {'detail': f'Deleted publisher {publisher_id}'}