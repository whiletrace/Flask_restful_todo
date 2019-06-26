from todo_api import create_app
import os


def test_create_app():
    """
    tests application factory

    first assertion tests that the application
    configuration id noy testing when application factory is instantiated
    second assertion tests that the testing configuration can be initialized
    on the application factory when set

    """
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_config(app):
    """
    tests that pytest fixtures can be passed to tests

    verifies that test configuration file is being found
    and that pytest fixtures can be passed to tests
    application configuration is 'TESTING'
    for unit tests via pytest fixture

    """
    assert app.testing


def test_client(client):
    """tests if URLs are being successfully bound to functions"""

    response = client.get('/hello')
    assert response.data == b'Hello World'
    assert response.status == '200 OK'


