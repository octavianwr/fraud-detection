import pytest
from app.app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_status(client):
    response = client.get('/status')
    assert response.status_code == 200
    assert "running" in response.json["status"].lower()
