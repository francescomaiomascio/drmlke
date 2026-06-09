from drmlke_provider.main import app
from fastapi.testclient import TestClient


def test_provider_health_live_trading_disabled() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["provider"] == "stub"
    assert response.json()["live_trading_enabled"] is False


def test_provider_models_empty() -> None:
    client = TestClient(app)

    response = client.get("/models")

    assert response.status_code == 200
    assert response.json() == {"models": []}
