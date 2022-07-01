from fastapi.testclient import TestClient

from backend.core.config import settings


def test_get_dataset(
        client: TestClient) -> None:
    client_path = 'dataset_one.csv'
    credit_path = 'dataset_two.csv'
    response = client.get(
        f"{settings.API_V1_STR}/datasets?client_path={client_path}&credit_path={credit_path}"
    )
    assert response.status_code == 200
