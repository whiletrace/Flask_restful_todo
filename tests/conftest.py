import pytest
import coverage
from peewee import *

from todo_api.models import Todo
from todo_api import create_app

Model = [Todo]

TEST_DATABASE = SqliteDatabase(':memory:')


@pytest.fixture
def initialize_test_db():
    TEST_DATABASE.bind(Model)
    TEST_DATABASE.connect()
    TEST_DATABASE.create_tables(Model, safe=True)
    yield initialize_test_db
    print('teardown of test db')
    TEST_DATABASE.close()


@pytest.fixture
def app():
    app = create_app({
       'TESTING': True
       })

    with app.app_context():
        initialize_test_db()

    return app


@pytest.fixture
def test_client(app):
    return app.test_client()


