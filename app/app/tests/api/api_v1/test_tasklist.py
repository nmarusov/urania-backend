from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_request(client: TestClient, user_token_headers: dict) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/tasklist/test_get",
        headers=user_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["msg"] == "Tasklist GET"


def test_post_request(client: TestClient, user_token_headers: dict) -> None:
    data = {"msg": "Test POST request"}
    response = client.post(
        f"{settings.API_V1_STR}/tasklist/test_post",
        headers=user_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["msg"] == f"Tasklist POST - {data['msg']}"
