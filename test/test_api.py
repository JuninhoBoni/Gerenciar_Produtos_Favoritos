from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

username = 'teste'
password = 'secret'

response_token = client.post(
    f"/token/?username={username}&password={password}")

Authorization = {
    "Authorization": f"{response_token.json()['token_type']} {response_token.json()['access_token']}"}


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Este projeto não contém front-end"}


def test_request_token():
    assert response_token.status_code == 200
    assert response_token.json()['token_type'] == "bearer"


email = 'teste@teste.com'
name = 'Teste'


def test_post_client():
    response = client.post(
        f"/clients/?name={name}&email={email}", headers=Authorization)
    assert response.status_code == 200
    assert response.json()['code'] == "success"


def test_post_client_error_404():
    response = client.post(
        f"/clients/?name={name}&email={email}", headers=Authorization)
    assert response.status_code == 404
    assert response.json()['detail']['code'] == "error"


name = 'Teste1'


def test_put_client():
    response = client.put(
        f"/clients/{name}/email/{email}", headers=Authorization)
    assert response.status_code == 200
    assert response.json()['code'] == "success"


email = 'teste0@teste0.com'


def test_put_client_error_404():
    print(f"/clients/{name}/email/{email}")
    response = client.put(
        f"/clients/{name}/email/{email}", headers=Authorization)
    assert response.status_code == 404
    assert response.json()['detail']['code'] == "error"


def test_get_client():
    response = client.get(
        f"/clients/{email}", headers=Authorization)
    assert response.status_code == 200
    assert response.json()['code'] == "success"


email_inexistente = 'teste1@teste1.com'


def test_get_client_error_404():
    response = client.get(
        f"/clients/{email_inexistente}", headers=Authorization)
    assert response.status_code == 404
    assert response.json()['detail']['code'] == "error"


def test_delete_client():
    response = client.delete(
        f"/clients/{email}", headers=Authorization)
    assert response.status_code == 200
    assert response.json()['code'] == "success"


def test_delete_client_error_404():
    response = client.delete(
        f"/clients/{email}", headers=Authorization)
    assert response.status_code == 404
    assert response.json()['detail']['code'] == "error"


email_422 = 'juninhoboni_gmail.com'


def test_post_client_error_422():
    response = client.post(
        f"/clients/?name={name}&email={email_422}", headers=Authorization)
    assert response.status_code == 422
    assert response.json()['detail'][0]['type'] == "value_error.email"


def test_put_client_error_422():
    response = client.put(
        f"/clients/{name}/email/{email_422}", headers=Authorization)
    assert response.status_code == 422
    assert response.json()['detail'][0]['type'] == "value_error.email"


def test_get_client_error_422():
    response = client.get(
        f"/clients/{email_422}", headers=Authorization)
    assert response.status_code == 422
    assert response.json()['detail'][0]['type'] == "value_error.email"


def test_delete_client_error_422():
    response = client.delete(
        f"/clients/{email_422}", headers=Authorization)
    assert response.status_code == 422
    assert response.json()['detail'][0]['type'] == "value_error.email"
