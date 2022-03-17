from app.models import (
    Authors,
    Books,
    cartItem,
    CreditCards,
    Orders,
    Publishers,
    ShoppingCart,
    Users,
    WishList
)
import pytest
from app.db import database

def get_name_of_user_from_userID(author_id:int):
    user_name_byID = Authors.get_author(author_id)
    return user_name_byID