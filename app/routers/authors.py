from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models.authors as model
import schemas.authors as schema

router = APIRouter(
    prefix='/api/authors',
    tags=['Authors']
)


@router.post('/', status_code = status.HTTP_201_CREATED)
def create_author(author: schema.Authors, db: Session = Depends(get_db)):
    
    try:
        new_author = model.Authors(
            id = len(db.query(model.Authors).all()) +1,
            first_name = author.first_name,
            last_name = author.last_name,
            biography = author.biography
        )
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
        return new_author
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Error => {e}')

@router.get('/')
def get_all_authors(db: Session = Depends(get_db)):
    authors = db.query(model.Authors).all()
    if not authors:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find any authors')
    return authors

@router.get('/{author_id}')
def get_author(author_id, db: Session = Depends(get_db)):
    author = db.query(model.Authors).filter(model.Authors.id == author_id).first()
    if not author:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with author_id: {author_id}')
    return author

@router.put('/{author_id}', status_code = status.HTTP_202_ACCEPTED)
def update_author(author_id, author: schema.Authors, db: Session = Depends(get_db)):
    author = db.query(model.Authors).filter(model.Authors.id == author_id).update({
        'firstName': author.first_name,
        'lastName': author.last_name,
        'biography': author.biography
    })
    if not author:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with author_id: {author_id}')
    db.commit()
    return {'detail': f'Update author {author_id}'}

@router.delete('/')
def delete_author(author_id, db: Session = Depends(get_db)):
    author = db.query(model.Authors).filter(model.Authors.id == author_id).first()
    if not author:
        raise HTTPException(status.HTTP_204_NO_CONTENT, f'No query found with author_id: {author_id}')
    db.delete(author)
    db.commit()
    return {'detail': f'Deleted author with id: {author_id}'}