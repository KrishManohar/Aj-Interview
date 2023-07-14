import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_get_random_python_response(client):
    response = client.get("/python")
    assert response.status_code == 200
    assert isinstance(response.json(), str)


def test_reverse_name_valid_string(client):
    response = client.get("/reverse/Krish")
    assert response.status_code == 200
    assert response.json() == {"letterCount": 5, "reversedName": "hsirK"}


def test_reverse_name_invalid_input(client):
    response = client.get("/reverse/123")
    assert response.status_code == 400
    assert response.json() == {"detail": "Name must contain only letters."}
