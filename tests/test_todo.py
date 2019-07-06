import json
from todo.models import Todo, db_wrapper

db = db_wrapper.database


def test_todo_list(client):

    rv = client.get('/api/v1/todos')
    json_data = rv.get_json()
    assert rv.status == '200 OK'


def test_get(client):
    file = open('../mock/todos.json', 'r')
    data = json.loads(file.read())
    print(data)
    with db.atomic():
        Todo.insert_many(data).execute()

    rv = client.get('/api/v1/todos')
    json_data = rv.get_json()
    assert json_data == [{'id': 1, 'name': 'clean the house'},
                                  {'id': 2, 'name': 'water the dog'},
                                  {'id': 3, 'name': 'feed the lawn'},
                                  {'id': 4, 'name': 'pay dem bills'},
                                  {'id': 5, 'name': 'run'},
                                  {'id': 6, 'name': 'swim'}]

    assert rv.status == '200 OK'


def test_post(client):
    rv = client.post('/api/v1/todos', json={'name': 'cleaning the hippos'})
    json_data = rv.get_json()
    assert json_data['name'] == 'cleaning the hippos'
    assert rv.status == '201 CREATED'


def test_404(client):
    rv = client.put('api/v1/todos/1', json={'name': 'cleaning the hippos'})
    json_response = rv.get_json()
    assert json_response['message']
    assert rv.status == '404 NOT FOUND'


def test_put(client):
    todo = Todo.create(name='this is a test')
    assert todo.name is 'this is a test'
    assert todo.id is 1

    rv = client.put('api/v1/todos/1', json={'name': 'cleaning the hippos'})
    json_response = rv.get_json()
    assert json_response['name'] == 'cleaning the hippos'
    assert json_response['id'] == 1
    assert rv.status_code == 201


def test_delete(client):
    todo = Todo.create(name='this is a test')
    assert todo.name is 'this is a test'
    assert todo.id is 1

    rv = client.delete('api/v1/todos/1')
    assert rv.status_code == 204
