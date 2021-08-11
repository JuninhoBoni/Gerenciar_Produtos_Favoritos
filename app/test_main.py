from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_item():
    response = client.get("/", headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTYyODcwMzczMn0.bgjQnGjH2OTVUC5BnQCKYV8acb8fRdnWspieJSTJeI8"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_token():
    response = client.post("/token?grant_type=&username=teste&password=secret&scope=&client_id=&client_secret=", 
            headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTYyODcwMzczMn0.bgjQnGjH2OTVUC5BnQCKYV8acb8fRdnWspieJSTJeI8"},
    )
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
