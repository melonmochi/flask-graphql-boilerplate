def test_hello(client):
    hello = client.get('/hello')
    assert b'Hello, World!' in hello.data
