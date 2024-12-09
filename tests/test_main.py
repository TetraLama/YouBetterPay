from fastapi.testclient import TestClient
from app.server.app import app  # Import de l'application principale

client = TestClient(app)

def test_read_root():
    """Test du point de terminaison racine (GET /)"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to this fantastic app!"}