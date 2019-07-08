from todo import models, db_wrapper

db = db_wrapper.database


def test_db(app):
    """
    asserts tests use the in memory test_database

    :param app: Flask application  in test config
    :type app: object
    """
    assert app.config['DATABASE'] == 'sqlite:///:memory:'


def test_todo_create(client):
    """
    tests of models and database logic

    asserts object is instance of correct class
    asserts object name attribute has expected value
    asserts object has an id attribute
    asserts objects.id is expected value
    :param client: flask test_client
    :type client: object
    """
    # creates Model.Todo object
    with db.atomic():
        todo = models.Todo.create(name='Shopping')

    assert isinstance(todo, models.Todo)
    assert todo.name == 'Shopping'
    assert hasattr(todo, 'id')
    assert todo.id is 1
