from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    '''This test should fail, the hello route is written to return "Greetings, World"'''
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
