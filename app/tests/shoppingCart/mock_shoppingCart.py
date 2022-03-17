from pickletools import uint4
from unittest import mock
from uuid import uuid4
from datetime import date
import pytest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.models.shoppingCart import ShoppingCart

@pytest.fixture
def flask_app_mock():
    #  flask application setup
    app_mock = Flask(__name__)
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock

@pytest.fixture
def mock_shoppingcart():
    new_shoppingcart = ShoppingCart(
        id = uuid4(),
        user_id = uuid4(),
        cart_item_id = uuid4()
    )
    return new_shoppingcart

@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock