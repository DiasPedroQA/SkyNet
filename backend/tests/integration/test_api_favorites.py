from fastapi.testclient import TestClient
from app.main import app
from app.models.favorite import Favorite
from app.repositories.favorite_repo import FavoriteRepo

client = TestClient(app)

def test_create_favorite():
    response = client.post("/api/v1/favorites/", json={"name": "Test Favorite", "url": "http://example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "Test Favorite"

def test_read_favorite():
    response = client.get("/api/v1/favorites/1")
    assert response.status_code == 200
    assert "name" in response.json()

def test_update_favorite():
    response = client.put("/api/v1/favorites/1", json={"name": "Updated Favorite", "url": "http://example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Favorite"

def test_delete_favorite():
    response = client.delete("/api/v1/favorites/1")
    assert response.status_code == 204
    assert response.content == b""