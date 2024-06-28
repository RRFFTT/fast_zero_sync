from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserPublicSchema, UserSchema

database = []  # FAKE DB

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)
    return user_with_id


@app.get(
    path='/retornohtml', status_code=HTTPStatus.OK, response_class=HTMLResponse
)
def exaula2():
    return """
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
