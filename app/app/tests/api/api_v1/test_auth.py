from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_access_token(client: TestClient) -> None:
    login_data = {
        "username": settings.TEST_USER_LOGIN,
        "password": settings.TEST_USER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/auth/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


def test_use_access_token(
    client: TestClient, user_token_headers: Dict[str, str]
) -> None:
    r = client.post(
        f"{settings.API_V1_STR}/auth/test-token",
        headers=user_token_headers,
    )
    result = r.json()
    assert r.status_code == 200
    assert "login" in result


def test_get_user_me(client: TestClient, user_token_headers: Dict[str, str]) -> None:
    r = client.get(f"{settings.API_V1_STR}/auth/me", headers=user_token_headers)
    current_user = r.json()
    assert current_user
    assert current_user["login"] == settings.TEST_USER_LOGIN
    assert current_user["full_name"] == settings.TEST_USER_FULL_NAME
