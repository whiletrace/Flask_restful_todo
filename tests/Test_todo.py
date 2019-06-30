
def test_todo_list(client, ):

    rv = client.get('/api/v1/todos')
    json_data = rv.get_json()
    assert rv.status == '200 OK'