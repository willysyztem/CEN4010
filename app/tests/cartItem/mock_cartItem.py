from unittest import mock
from uuid import uuid4
import pytest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.models.cartItem import cartItem

@pytest.fixture
def flask_app_mock():
    #  flask application setup
    app_mock = Flask(__name__)
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock

@pytest.fixture
def mock_cartItem():
    new_cartItem = cartItem(
        id = uuid4(),
        shoppingcart_id = uuid4(),
        book_id = uuid4(),
        book_title = 'arbitrary bookTitle'
    )
    return new_cartItem

@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock