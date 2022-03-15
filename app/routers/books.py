from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db

import models.books as model
import schemas.books as schema

import utils, oauth2

router = APIRouter(
    prefix = '/api/books',
    tags=['Books Management']
)

@router.get('/')
def get_all_books(db: Session = Depends(get_db)):
    book = db.query(model.Books).all()
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find books')
    return book

@router.get('/{isbn}')
def get_books(isbn, db: Session = Depends(get_db)):
    book = db.query(model.Books).filter(model.Books.isbn == isbn).first()
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with isbn: {isbn}')
    return book

@router.put('/{isbn}', status_code=status.HTTP_202_ACCEPTED)
def update_book(isbn, book: schema.Books, db: Session = Depends(get_db)):
    updated_book = db.query(model.Books).filter(model.Books.isbn == isbn).update({
        'isbn': book.isbn,
        'title': book.title,
        'author_id': book.author_id,
        'description': book.description,
        'publisher': book.publisher,
        'publishDate': book.publishedDate,
        'copiesSold': book.copiesSold,
        'price': book.price
    })
    if not updated_book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with isbn: {isbn}')
    db.commit()
    return {'detail': f'Update book {isbn}'}