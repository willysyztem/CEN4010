from unittest import mock
from uuid import uuid4
from datetime import date
import pytest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.models.books import Books

@pytest.fixture
def flask_app_mock():
    #  flask application setup
    app_mock = Flask(__name__)
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock

@pytest.fixture
def mock_book():
    new_book = Books(
        id = uuid4(),
        isbn =  12345,
        title = 'arbitrary title',
        author_id = uuid4(),
        publisher_id = uuid4(),
        publishedDate = date.today(),
        description = 'arbitrary description',
        price = 12,
        copiesSold = 10
    )
    return new_book

@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock