from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # (A) ACT (ação)

    assert (
        response.status_code == HTTPStatus.OK
    )  # (A) Garantir que esta funcionado
    assert response.json() == {'message': 'Olá mundo!'}


def test_retornohtml_deve_retornar_ok_e_o_codigo_html(client):
    response = client.get(url='/retornohtml')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <!DOCTYPE html>
    <html lang="pt-br">
      <head>
        <title>Aula 2 - Dunossauro FastApi</title>
        <meta charset="utf-8">
      </head>
      <body>
        <h1>Olá Mundo!<br>Exercicio aula 2!</h1>
      </body>
    </html>
    """
    )


def test_create_user(client):
    client_test_post = {
        'username': 'testeusername',
        'password': 'password',
        'email': 'test@test.com',
    }

    response = client.post(
        '/users/',
        json=client_test_post,
    )

    client_test_response = {'id': 1}
    client_test_response |= {
        key: value
        for key, value in client_test_post.items()
        if key != 'password'
    }

    # Validar se o retorno é 201
    assert response.status_code == HTTPStatus.CREATED

    # Validar se UserPublic retorna o esperado
    assert response.json() == client_test_response
