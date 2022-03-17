from unittest import mock
from uuid import uuid4
from datetime import date
import pytest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.models.orders import Orders

@pytest.fixture
def flask_app_mock():
    #  flask application setup
    app_mock = Flask(__name__)
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock

@pytest.fixture
def mock_orders():
    new_order = Orders(
        id = uuid4(),
        orderDate = date.today(),
        subtotal = 10,
        shipping = 2,
        user_id = uuid4()
    )
    return new_order

@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock