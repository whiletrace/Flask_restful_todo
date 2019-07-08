import json
from todo.models import Todo, db_wrapper

db = db_wrapper.database


def test_get(client):
    """
    tests get method for endpoint /api/v1/todos

    from file load dummy data and insert to test database
    and then test_client performs get request to endpoint
    assert response from endpoint is what is expected:
    response body is correct json content
    and that response status code is 200

    :param client: Flask test_client
    :type client: object
    """
    try:
        file = open('mock/todos.json', 'r')
    except FileNotFoundError:
        file = open('../mock/todos.json', 'r')

    data = json.loads(file.read())

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

    assert rv.status_code == 200


def test_post(client):
    """
    tests post method for endpoint /api/v1/todos

    test_client performs post request to endpoint with dummy data
    assert response from endpoint is what is expected:
    response body contains correct json content
    and that response status code is 201 w

    :param client: Flask test_client
    :type client: object
    """
    rv = client.post('/api/v1/todos', json={'name': 'cleaning the hippos'})
    json_data = rv.get_json()
    assert json_data['name'] == 'cleaning the hippos'
    # 201 :request fulfilled and resource has been created
    assert rv.status_code == 201


def test_404(client):
    """
    tests endpoint executes correct function upon a exception

    test_client performs put request to endpoint where the resource does not exist
    assert response from endpoint is what is expected:
    response body contains message
    and that response status code is 404

    :param client: Flask test_client
    :type client: object
    """
    rv = client.put('api/v1/todos/1', json={'name': 'cleaning the hippos'})
    json_response = rv.get_json()
    assert json_response['message']
    assert rv.status_code == 404


def test_put(client):
    """
    tests put method for endpoint 'api/v1/todos/<int:id>

    create and insert object into test db table
    assert object has expected attributes and attributes have expected values
    test_client performs put request to endpoint for resource with id of 1

    assert response from endpoint is what is expected:
    response body attr values are correct:
    and that response status code is 201

    :param client: Flask test_client
    :type client: object
    """
    todo = Todo.create(name='this is a test')
    assert todo.name is 'this is a test'
    assert todo.id is 1

    rv = client.put('api/v1/todos/1', json={'name': 'cleaning the hippos'})
    json_response = rv.get_json()
    assert json_response['name'] == 'cleaning the hippos'
    assert json_response['id'] == 1
    assert rv.status_code == 201


def test_delete(client):
    """
    tests delete method for endpoint 'api/v1/todos/<int:id>

    create and insert object into test db table
    assert object has expected attributes and attributes have expected values
    test_client performs delete request to endpoint for resource with id of 1

    assert response from endpoint is what is expected:
    response status code is 204

    :param client: Flask test_client
    :type client: object
    """

    todo = Todo.create(name='this is a test')
    assert todo.name is 'this is a test'
    assert todo.id is 1

    rv = client.delete('api/v1/todos/1')
    assert rv.status_code == 204
