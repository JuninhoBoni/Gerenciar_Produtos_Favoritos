from fastapi.testclient import TestClient

from api import app

client = TestClient(app)

def test_read_item():
    response = client.get("/", headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTYyODcyMzIxOH0.AWo88LtqU8QHrdvelQ1-ucYyC5zaztLGX8kVJoi7zBs"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

