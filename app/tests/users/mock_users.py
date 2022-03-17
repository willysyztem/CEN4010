from unittest import mock
from uuid import uuid4
import pytest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.models.users import Users

@pytest.fixture
def flask_app_mock():
    #  flask application setup
    app_mock = Flask(__name__)
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock

@pytest.fixture
def mock_user():
    new_user = Users(
        id = uuid4(),
        email = 'arbitraryemail@arbitrary.com',
        password = 'arbitrary password',
        username = 'arbitrary username',
        name = 'arbitrary name',
        home_address = 'arbitrary address'
    )
    return new_user

@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock