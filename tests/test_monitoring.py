from fastapi.testclient import TestClient
from src.main import app
from src.datamodels.monitor import HealthStatus


client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()
    assert response.json().get("status") == HealthStatus.status_pass


def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
