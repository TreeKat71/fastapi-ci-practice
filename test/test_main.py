from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_query_name():
    name = "muller"
    response = client.get(f"/query?name={name}")
    assert response.status_code == 200
    assert response.json() == {"name": name}
