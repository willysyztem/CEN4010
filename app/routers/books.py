from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db

import models.books as model
import schemas.books as schema

router = APIRouter(
    prefix = '/api/books',
    tags=['Books Management']
)

@router.get('/')
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(model.Books).all()
    if not books:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find books')
    return books

@router.get('/')
def get_bestsellers(db: Session = Depends(get_db)):
    books = db.query(model.Books).order_by(model.Books.copies_sold.desc()).limit(12).all()
    if not books:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find books')
    return books


@router.get('/{isbn}')
def get_book_by_isbn(isbn, db: Session = Depends(get_db)):
    book = db.query(model.Books).filter(model.Books.isbn == isbn).first()
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with isbn: {isbn}')
    return book

@router.get('/{book_id}')
def get_book_by_id(book_id, db: Session = Depends(get_db)):
    book = db.query(model.Books).filter(model.Books.id == book_id).first()
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with id: {book_id}')
    return book

@router.put('/{isbn}', status_code = status.HTTP_202_ACCEPTED)
def update_book(isbn, book: schema.Books, db: Session = Depends(get_db)):
    updated_book = db.query(model.Books).filter(model.Books.isbn == isbn).update({
        'title' : book.title,
        'published_date' : book.publisher_id,
        'description' : book.description,
        'price' : book.price,
        'copies_sold' : book.copies_sold,
        'author_id' : book.author_id,
        'publisher_id' : book.publisher_id
    })
    if not updated_book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with isbn: {isbn}')
    db.commit()
    return {'detail': f'Update book {isbn}'}