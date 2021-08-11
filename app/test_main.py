from fastapi.testclient import TestClient

from main import app

test = TestClient(app)

def test_read_item():
    response = test.get(f"/clients/aa@aaa.com.ve", headers={"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNjI4Njc5ODQzfQ.6q5hzkxQeJIDNHChocjO1E3ECq-mGq-6Ofcd9hW9Bx4"})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
