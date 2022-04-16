from fastapi import APIRouter

# Import all routers (apis)
from routers import auth, authors, books, creditcards, orders, publishers, shoppingcart, users, wishlist, route_endpoints

main_router = APIRouter()

main_router.include_router(auth.router)
main_router.include_router(authors.router)
main_router.include_router(books.router)
main_router.include_router(creditcards.router)
main_router.include_router(orders.router)
main_router.include_router(publishers.router)
main_router.include_router(shoppingcart.router)
main_router.include_router(users.router)
main_router.include_router(wishlist.router)
main_router.include_router(route_endpoints.router)