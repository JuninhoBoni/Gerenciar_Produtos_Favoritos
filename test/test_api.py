from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

username = 'teste'
password = 'secret'
email = 'juninhoboni@gmail.com'
name = 'Daniel Dias'

response_token = client.post(
    f"/token/?username={username}&password={password}")

Authorization = {"Authorization": f"{response_token.json()['token_type']} {response_token.json()['access_token']}"}

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Este projeto não contém front-end"}


def test_request_token():
    assert response_token.status_code == 200
    assert response_token.json()['token_type'] == "bearer"


def test_post_client():
    print(Authorization)
    response = client.post(
        f"/clients/?name={name}&email={email}", headers = Authorization)
    assert response.status_code == 200
    assert response.json()['code'] == "success"

def test_post_client_error_404():
    print(Authorization)
    response = client.post(
        f"/clients/?name={name}&email={email}", headers = Authorization)
    assert response.status_code == 404
    assert response.json()['detail']['code'] == "error"
