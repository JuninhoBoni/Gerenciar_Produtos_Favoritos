from fastapi.testclient import TestClient
import json
from api import app

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Este projeto não contém front-end"}

def test_request_token():
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
            'username':'teste', 
            'password':'secret'
    }

    response = client.post("/token/", data=json.dumps(data), headers=headers)
    assert response.status_code == 200
    #assert response.json() == {"msg": "Este projeto não contém front-end"}
'''def test_read_item():
    response = client.get("/", headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTYyODcyMzIxOH0.AWo88LtqU8QHrdvelQ1-ucYyC5zaztLGX8kVJoi7zBs"})
    assert response.status_code == 200
    assert response.json() == {"msg": "Este projeto não contém front-end"}
'''
