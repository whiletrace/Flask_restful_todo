import pytest
from flask import Flask

from todo_api import create_app


@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config['TESTING'] = True

    return app


@pytest.fixture
def client(app):
    return app.test_client()
