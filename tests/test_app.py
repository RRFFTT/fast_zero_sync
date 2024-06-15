from http import HTTPStatus
from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app) #(A) ARRANGE (organização)
    response = client.get('/') # (A) ACT (ação)

    assert response.status_code == HTTPStatus.OK # (A) Garantir que esta funcionado
    assert response.json() == {'message': 'Olá mundo!'}
    ...
