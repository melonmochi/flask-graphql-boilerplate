def test_departments(client):
    response = client.get('/departments')
    assert response.status_code == 200
