from fastapi import APIRouter, Request, status, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
from db.database import get_db

# router imports
from routers.books import get_bestsellers, get_book_by_isbn
from routers.authors import get_author
from routers.publishers import get_publisher
from routers.creditcards import get_user_creditcards
from routers.wishlist import get_wishlist
from routers.shoppingcart import get_shoppingcart
from routers.auth import manager

templates = Jinja2Templates(directory='./templates')
router = APIRouter(include_in_schema=False)

# login page
@router.get('/login')
def get_login_page(request: Request):
    return templates.TemplateResponse('endpoints/login.html', {'request': request})

# register page
@router.get('/register')
def register_page(request: Request):
    return templates.TemplateResponse('endpoints/register.html', {'request': request})

# home page
@router.get('/index')
def get_home_page(request: Request, db: Session = Depends(get_db), user=Depends(manager)):
    books = get_bestsellers(db)
    return templates.TemplateResponse('endpoints/index.html', {'request': request, 'books': books, 'user': user})

# book page
@router.get('/book/{isbn}')
def get_book_page(isbn, request: Request, db: Session = Depends(get_db), user=Depends(manager)):
    book = get_book_by_isbn(isbn, db)
    author = get_author(book.author_id, db)
    publisher = get_publisher(book.publisher_id, db)
    wishlists = get_wishlist(user.id, db)
    return templates.TemplateResponse('endpoints/book_page.html', {'request': request, 'book': book, 'author': author, 'publisher': publisher, 'wishlists': wishlists,'user': user})

# user page
@router.get('/api/user/{username}')
def get_user_page(request: Request, db: Session = Depends(get_db), user=Depends(manager)):
    creditcard = get_user_creditcards(user.id, db)
    return templates.TemplateResponse('endpoints/user_page.html', {'request': request, 'user': user, 'creditcard': creditcard})

# wishlist page
@router.get('/api/wishlist')
def get_user_wishlist(request: Request, db: Session = Depends(get_db), user=Depends(manager)):
    wishlists = get_wishlist(user.id, db)
    return templates.TemplateResponse('endpoints/wishlist_page.html', {'request': request, 'user': user, 'wishlists': wishlists})

# shoppingcart page
@router.get('/api/cart')
def get_user_wishlist(request: Request, db: Session = Depends(get_db), user=Depends(manager)):
    shoppingcart = get_shoppingcart(user.id, db)
    return templates.TemplateResponse('endpoints/shoppingcart_page.html', {'request': request, 'user': user, 'shoppingcart': shoppingcart})

# catalog page
@router.get('/catalog')
def get_catalog(request: Request, db: Session = Depends(get_db), user=Depends(manager)):
    books = get_bestsellers(db)
    return templates.TemplateResponse('endpoints/catalog.html', {'request': request, 'user': user, 'books': books})