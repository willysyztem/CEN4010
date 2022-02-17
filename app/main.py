from fastapi import FastAPI, Depends, status, HTTPException
from app.db.models import Author, Book, User, Publisher, Orders
from app.schemas.users_schema import AuthorSchema, BookSchema, UserSchema, PublisherSchema, OrderSchema

# Settings For Fast API & DB
from config.settings import settings

# DB
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine

# Create Table
# DO NOT DELETE BASE
from db.models import Base
Base.metadata.create_all(bind=engine)
# Import the rest of the models under here
from db.models import User

# Schema
from schemas.users_schema import UserSchema

#Gets the Database DONT DELETE
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Boilerplate stuff for fastapi
def start_app():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        version=settings.PROJECT_VERSION
    )

    return app
app = start_app()

# Put your creating APIS/ENDPOINT UNDER HERE
#
# Root Welcome Message
@app.get('/')
def root():
    return 'This is the root page, use /docs to use restfulAPI'

# PROFILE MANAGEMENT
@app.post('/api/users', status_code=status.HTTP_201_CREATED)
def create_users(user: UserSchema, db: Session = Depends(get_db)):
    new_user = User(
        email_address = user.email,
        password = user.password,
        username = user.email,
        name = user.name,
        home_address = user.home_address
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='User already exists')

# ---------------------
# Users

@app.get('/api/users')
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find users')
    return users

@app.get('/api/users/{username}')
def get_user(username, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with username: {username}')
    return user

@app.put('/api/users/{username}', status_code=status.HTTP_202_ACCEPTED)
def update_user(username, user: UserSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).update({
        'password': user.password,
        'name': user.name,
        'home_address': user.home_address
    })
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with username: {username}')
    db.commit()
    return {'detail': f'Update user {username}'}

# ---------------------
# Books

@app.get('/api/books')
def get_all_books(db: Session = Depends(get_db)):
    book = db.query(User).all()
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find books')
    return book

@app.get('/api/books/{isbn}')
def get_user(isbn, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.isbn == isbn).first()
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with isbn: {isbn}')
    return book

@app.put('/api/books/{isbn}', status_code=status.HTTP_202_ACCEPTED)
def update_book(isbn, book: BookSchema, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.isbn == isbn).update({
        'isbn': book.isbn,
        'title': book.title,
        'author_id': book.author_id,
        'description': book.description,
        'publisher': book.publisher,
        'publishDate': book.publishedDate,
        'copiesSold': book.copiesSold,
        'price': book.price
    })
    if not book:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f'No query found with isbn: {isbn}')
    db.commit()
    return {'detail': f'Update book {isbn}'}

# ---------------------
# Authors

@app.get('/api/authors')
def get_all_books(db: Session = Depends(get_db)):
    author = db.query(Author).all()
    if not author:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find authors')
    return author


@app.get('/api/authors/{author_id}')
def get_user(author_id, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.author_id == author_id).first()
    if not author:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No query found with author: {author_id}')
    return author


@app.put('/api/authors/{author_id}', status_code=status.HTTP_202_ACCEPTED)
def update_author(author_id, author: AuthorSchema, db: Session = Depends(get_db)):
    author = db.query(Author).filter(Author.author_id == author_id).update({
        'author_id': author.author_id,
        'firstName': author.firstName,
        'lastName': author.lastName,
        'publisher': author.publisher,
        'biography': author.biography,
        'books': author.books
    })
    if not author:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f'No query found with author_id: {author_id}')
    db.commit()
    return {'detail': f'Update author {author_id}'}

# ---------------------
# Publishers

@app.get('/api/publishers')
def get_all_books(db: Session = Depends(get_db)):
    publisher = db.query(Publisher).all()
    if not publisher:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find publishers')
    return publisher


@app.get('/api/publishers/{publisher_id}')
def get_user(publisher_id, db: Session = Depends(get_db)):
    publisher = db.query(Publisher).filter(Publisher.publisher_id == publisher_id).first()
    if not publisher:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No query found with publisher: {publisher_id}')
    return publisher


@app.put('/api/publishers/{publisher_id}', status_code=status.HTTP_202_ACCEPTED)
def update_publisher(publisher_id, publisher: PublisherSchema, db: Session = Depends(get_db)):
    publisher = db.query(Publisher).filter(Publisher.publisher_id == publisher_id).update({
        'publisher_id': publisher.publisher_id,
        'book_id': publisher.book_id,
        'country': publisher.country
    })
    if not publisher:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f'No query found with publisher_id: {publisher_id}')
    db.commit()
    return {'detail': f'Update publisher {publisher_id}'}

# ---------------------
# Orders

@app.get('/api/orders')
def get_all_books(db: Session = Depends(get_db)):
    order = db.query(Orders).all()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Could not find orders')
    return order


@app.get('/api/orders/{order_id}')
def get_user(order_id, db: Session = Depends(get_db)):
    order = db.query(Orders).filter(Orders.order_id == order_id).first()
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND,f'No query found with order: {order_id}')
    return order


@app.put('/api/orders/{order_id}', status_code=status.HTTP_202_ACCEPTED)
def update_order(order_id, order: OrderSchema, db: Session = Depends(get_db)):
    order = db.query(Orders).filter(Orders.order_id == order_id).update({
        'order_id': order.order_id,
        'user_id': order.user_id,
        'orderDate': order.orderDate,
        'subtotal': order.subtotal,
        'shipping': order.shipping,
        'total': order.total
    })
    if not order:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            f'No query found with order_id: {order_id}')
    db.commit()
    return {'detail': f'Update order {order_id}'}
    