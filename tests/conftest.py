import pytest
from todo_api import create_app
from todo_api.models import Todo, db_wrapper



@pytest.fixture()
def app():

    app = create_app({
        'TESTING': True,
        'DATABASE': 'sqlite:///:memory:'
        })

    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    db_wrapper.init_app(app)
    test_db = db_wrapper.database
    Todo.bind(test_db)
    test_db.connect()
    Todo.create_table(safe=True)

    yield test_db

    test_db.close()
