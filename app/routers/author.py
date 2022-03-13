from fastapi import Depends, status, HTTPException, APIRouter

from typing import List

from sqlalchemy.orm import Session
from db.database import get_db

import models
import schemas

router = APIRouter(
    prefix='/api/authors',
    tags=['Authors']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Author)
def create_author(author: schemas.Author, db: Session = Depends(get_db)):
    try:
        new_author = models.Author(
            firstName=author.firstName,
            lastName=author.lastName,
            publisher=author.publisher,
            books=author.books,
            biography=author.biography
        )
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
        return new_author
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='author already exists')


@router.get('/',  response_model=List[schemas.Author])
def get_all_authors(db: Session = Depends(get_db)):
    authors = db.query(models.Author).all()
    if not authors:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find authors')
    return authors


@router.get('/{author_id}', response_model=schemas.Author)
def get_author(author_id, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.author_id == author_id).first()
    if not author:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with author_id: {author_id}')
    return author


@router.get('/{title}', response_model=schemas.Author)
def get_author(title, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.author_id == title).first()
    if not author:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with title: {title}')
    return author


@router.put('/{author_id}', status_code=status.HTTP_202_ACCEPTED)
def update_author(author_id, author: schemas.Author, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.author_id == author_id).update({
        'firstName': author.firstName,
        'lastName': author.lastName,
        'publisher': author.publisher,
        'books': author.books,
        'biography': author.biography
    })
    if not author:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with author_id: {author_id}')
    db.commit()
    return {'detail': f'Update author {author_id}'}


@router.delete('/')
def delete_author(author_id, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.author_id == author_id).first()
    if not author:
        raise HTTPException(status.HTTP_204_NO_CONTENT, f'No query found with author_id: {author_id}')
    db.delete(author)
    db.commit()
    return {'detail': f'Deleted author {author_id}'}