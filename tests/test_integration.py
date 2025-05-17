from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_assets():
    response = client.get("/assets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_metrics():
    response = client.get("/metrics/BTC")
    assert response.status_code == 200
    data = response.json()
    assert "symbol" in data
    assert data["symbol"] == "BTC"
