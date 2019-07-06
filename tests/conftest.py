import pytest
from todo import create_app
from todo.models import Todo, db_wrapper


@pytest.fixture()
def app():
    app = create_app({
        'TESTING': True,
        'DATABASE': 'sqlite:///:memory:'
        })

    return app


@pytest.fixture
def client(app):
    with app.app_context():
        test_database = db_wrapper.database
        db_wrapper.init_app(app)
        Todo.bind_ctx(test_database)
        Todo.create_table()

    yield app.test_client()

    test_database.close()

