from api.app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    
    data = response.json()

    assert data["status"] == "ok"
    assert data["environment"] == "development"