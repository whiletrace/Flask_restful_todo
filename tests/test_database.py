from todo_api import models


def test_db(app):

    assert app.config['DATABASE'] == 'sqlite:///:memory:'


def test_todo_create(db):
    todo = models.Todo.create(name='Shopping')

    assert isinstance(todo, models.Todo)
    assert todo.name == 'Shopping'
    assert hasattr(todo, 'id')
    assert todo.id is 1
