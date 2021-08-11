from fastapi.testclient import TestClient
from ..services.validate import ValidateToken

from ..main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/", headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTYyODcyMzIxOH0.AWo88LtqU8QHrdvelQ1-ucYyC5zaztLGX8kVJoi7zBs"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_token():
    response = client.post("/token?grant_type=&username=teste&password=secret&scope=&client_id=&client_secret=", 
            headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTYyODcyMzIxOH0.AWo88LtqU8QHrdvelQ1-ucYyC5zaztLGX8kVJoi7zBs"},
    )
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
