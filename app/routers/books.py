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
        'price': book.price,
        'genre': book.genre,
        'rating': book.rating
    })
    if not updated_book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with isbn: {isbn}')
    db.commit()
    return {'detail': f'Update book {isbn}'}


@router.get('/{genrename}')
def get_books_by_genre(genrename, db: Session = Depends(get_db)):
    booksbygenre = db.query(model.Books).filter(model.Books.genre == genrename).all()
    if not booksbygenre:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with genre: {genrename}')
    return booksbygenre


@router.get('/{numberofcopies}')
def get_books_by_copies_sold(numberofcopies, db: Session = Depends(get_db)):
    booksbycopies = db.query(model.Books).filter(model.Books.copiesSold == numberofcopies).all()
    if not booksbycopies:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with genre: {numberofcopies}')
    return booksbycopies

@router.get('/{bookrating}')
def get_books_by_rating(bookrating, db: Session = Depends(get_db)):
    booksbyrating= db.query(model.Books).filter(model.Books.rating == bookrating).all()
    if not booksbyrating:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with genre: {bookrating}')
    return booksbyrating