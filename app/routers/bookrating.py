from ast import Dict
from datetime import datetime
from fastapi import Depends, status, HTTPException, APIRouter

from sqlalchemy.orm import Session
from db.database import get_db

#Bookrating Model/Schema
import models.bookrating as model
import schemas.bookrating as schema

#Books class Router
import routers.books as booksRouter

router = APIRouter(
    prefix = '/api/bookrating',
    tags=['Book Rating and Commenting']
)

#TODO Get rating by user to validate user does not add duplicate ratings

#Book Ratings
@router.get('/allbooks')
def get_all_bookratings(db: Session = Depends(get_db)):
    bookratingtemp = db.query(model.BookRating).all()
    bookrating: list = []
    for i in bookratingtemp:
        bookrating.append(model.BookRating(
            user_id = i.id,
            book = booksRouter.get_book_by_isbn(i.book, db).title,
            rating = i.rating,
            created_at = i.created_at
        ))

    bookrating.sort(key=ratingSort, reverse=True)
    if not bookrating:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find book ratings')
    return bookrating

@router.post('', status_code=status.HTTP_201_CREATED)
def new_bookrating(isbn, newrating: int, userId, db: Session = Depends(get_db)):
    checkifbookexists(isbn, db)
    if newrating > 5 or newrating < 1:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, detail = 'Please enter a rating from 1 - 5')
    now = datetime.now()
    try:
        new_bookrating = model.BookRating(
            user_id = userId,
            book = booksRouter.get_book_by_isbn(isbn, db).isbn,
            rating = newrating,
            created_at = now.strftime("%m/%d/%Y, %H:%M:%S")
        )
        db.add(new_bookrating)
        db.commit()
        db.refresh(new_bookrating)
        return new_bookrating
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Failed creating new rating {e}')

@router.get('/averagerating')
def get_averagerating(isbn, db: Session = Depends(get_db)):
    checkifbookexists(isbn, db)
    allbookratings = db.query(model.BookRating).all()
    sumratings: int = 0
    bookratingcount: int = 0
    averagerating: int = 0
    returnstring: str = ""

    for i in allbookratings:
        if i.book == isbn:
            sumratings += i.rating
            bookratingcount += 1
    
    if (sumratings > 0 and bookratingcount > 0):
        averagerating = sumratings / bookratingcount

    if (averagerating > 0):
        returnstring = "Average Rating is " + '{:.2f}'.format(averagerating)
    return returnstring

#Book Comments
@router.get('/bookcomment')
def get_all_comments(db: Session = Depends(get_db)):
    bookcommenttemp = db.query(model.BookComment).all()
    bookcomment: list = []
    for i in bookcommenttemp:
        bookcomment.append(model.BookComment(
            user_id = i.id,
            book = booksRouter.get_book_by_isbn(i.book, db).title,
            comment = i.comment,
            created_at = i.created_at
        ))
    return bookcomment

@router.get('/bookcomment/{isbn}')
def get_comments_by_isbn(isbn, db: Session = Depends(get_db)):
    allbookcomments = db.query(model.BookComment).all()
    bookcomment: list = []
    for i in allbookcomments:
        if i.book == isbn:
            bookcomment.append(model.BookComment(
                user_id = i.id,
                book = booksRouter.get_book_by_isbn(i.book, db).title,
                comment = i.comment,
                created_at = i.created_at
            ))
    if not bookcomment:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail = 'Could not find book comments')
    return bookcomment

@router.post('/bookcomment', status_code=status.HTTP_201_CREATED)
def new_bookcomment(isbn, comment, userId, db: Session = Depends(get_db)):
    checkifbookexists(isbn, db)
    now = datetime.now()
    try:
        new_bookcomment = model.BookComment(
            user_id = userId,
            book = booksRouter.get_book_by_isbn(isbn, db).isbn,
            comment = comment,
            created_at = now.strftime("%m/%d/%Y, %H:%M:%S")
        )
        db.add(new_bookcomment)
        db.commit()
        db.refresh(new_bookcomment)
        return new_bookcomment
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail = f'Failed creating new comment {e}')

def ratingSort(ratings):
    return ratings.rating

def checkifbookexists(isbn, db):
    booksRouter.get_book_by_isbn(isbn, db)