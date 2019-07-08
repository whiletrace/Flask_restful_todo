import pytest
from todo import create_app
from todo.models import Todo, db_wrapper


@pytest.fixture()
def app():
    """
    returns a instance of the application object with testing config

    :var app: function
    :rtype: object: Flask_application
    """
    app = create_app({
        'TESTING': True,
        'DATABASE': 'sqlite:///:memory:'
        })

    return app


@pytest.fixture
def client(app):
    """
    Instantiates an instance of the flask test_client and Test database

    this provides a test_client to each test which allows access
    to the Http request and response also
    initializes a in memory test_database
    for tests
    :return flask test_client
    :rtype: object
    :param app: Flask_application test configuration
    :type app: object
    """
    # setup
    with app.app_context():
        """test_database = db_wrapper.database
        db_wrapper.init_app(app)
        test_database.connect()
        Todo.bind_ctx(test_database)
        Todo.create_table()
        """
    return app.test_client()
    # teardown

