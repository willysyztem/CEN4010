from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy import func
from sqlalchemy.orm import Session
from db.database import get_db

import models.books as model
import schemas.books as schema

router = APIRouter(
    prefix = '/api/books',
    tags=['Books Management']
)

@router.post('/', include_in_schema=False)
def create_book(book: schema.Books, db: Session = Depends(get_db)):
    try:
        new_book = model.Books(
            id = len(db.query(model.Books).all()) +1,
            isbn =  book.isbn,
            title = book.title,
            published_date = book.published_date,
            description = book.description,
            price = book.price,
            copies_sold = book.copies_sold,
            author_id = book.author_id,
            publisher_id = book.publisher_id,
            genre = book.genre,
            pages = book.pages
        )
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return {'detail': f'Book Created'}
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Error => {e}')


@router.get('/all')
def get_all_books(db: Session = Depends(get_db)):
    books = db.query(model.Books).all()
    if not books:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find books')
    return books

@router.get('/bestseller')
def get_bestsellers(db: Session = Depends(get_db)):
    books = db.query(model.Books).order_by(model.Books.copies_sold.desc()).limit(10).all()
    if not books:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find books')
    return books

@router.get('/{limit}')
def get_books_with_limit(limit: int, db: Session = Depends(get_db)):
    books = db.query(model.Books).limit(limit).all()
    if not books:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find books')
    return books

@router.get('/genre')
def get_book_by_genre(genre: str, db: Session = Depends(get_db)):
    books = db.query(model.Books).filter(func.lower(model.Books.genre) == func.lower(genre)).all()
    if not books:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Could not find books with genre {genre}')
    return books

@router.get('/author/{author_id}')
def get_book_by_author(author_id: int, db: Session = Depends(get_db)):
    books = db.query(model.Books).filter(model.Books.author_id == author_id).all()
    if not books:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = f'Could not find books by author with ID {author_id}')
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