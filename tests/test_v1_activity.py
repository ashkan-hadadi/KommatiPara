from fastapi.testclient import TestClient
import backend

client = TestClient(backend)


def test_activity():
    response = client.post("http://0.0.0.0:8000/api/v1/activity/")
    assert response.status_code == 204
