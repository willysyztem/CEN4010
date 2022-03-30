from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db

#Bookrating Model/Schema
import models.bookrating as model
import schemas.bookrating as schema

#Books class Router
import routers.books as books

router = APIRouter(
    prefix = '/api/bookrating',
    tags=['Book Rating and Commenting']
)

#Book Ratings
@router.get('/')
def get_all_bookratings(db: Session = Depends(get_db)):
    bookrating = db.query(model.BookRating).all()
    if not bookrating:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find book ratings')
    return bookrating

@router.post('/', status_code=status.HTTP_201_CREATED, response_model = schema.BookRating)
def new_bookrating(isbn, bookrating: schema.BookRating, db: Session = Depends(get_db)):
    try:
        new_bookrating = model.BookRating(
            bookrating_id = bookrating.id,
            book = books.get_book(isbn),
            rating = bookrating.rating,
            created_at = bookrating.created_at
        )
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = 'Order already exists')
