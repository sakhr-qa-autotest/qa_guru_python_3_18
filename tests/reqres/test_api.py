import allure
from pytest_voluptuous import S

from schemas.user import user


def test_status_code(reqres):
    with allure.step('Status code'):
        response = reqres.get('users?page=1')
        assert response.status_code == 200


def test_schema(reqres):
    with allure.step('Schema'):
        response = reqres.get('users/2')
        assert S(user) == response.json()['data']


def test_login_successful(reqres):
    with allure.step('Login successful'):
        response = reqres.post('login', json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })

    assert response.status_code == 200
    assert len(response.json().get('token')) >= 1


def test_login_unsuccessful(reqres):
    with allure.step('Login unsuccessful'):
        response = reqres.post('login', json={
            "email": "eve.holt@reqres.in"
        })

        assert response.status_code == 400
        assert response.json().get('error') >= 'Missing password'


def test_create_successful(reqres):
    with allure.step('Create successful'):
        response = reqres.post('users', json={
            "id": 999,
            "email": "test@user.ru",
            "password": "123"
        })

        assert response.status_code == 201
        assert response.reason == 'Created'
