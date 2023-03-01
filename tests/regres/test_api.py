import allure
from pytest_voluptuous import S

from schemas.user import user
from utils.base_session import regres

mainUrl = 'https://reqres.in/api/'
testUser = {
    "id": 999,
    "email": "test@user.ru",
    "password": "123"
}


def test_status_code():
    with allure.step('Check status code'):
        response = regres.get('users?page=1')

        assert response.status_code == 200


def test_schema():
    with allure.step('Schema'):
        response = regres.get('users/2')
        assert S(user) == response.json()['data']


def test_login_successful():
    with allure.step('Login successful'):
        response = regres.post('login', json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })

    assert response.status_code == 200
    assert len(response.json().get('token')) >= 1


def test_login_unsuccessful():
    with allure.step('Login unsuccessful'):
        response = regres.post('login', json={
            "email": "eve.holt@reqres.in"
        })

        assert response.status_code == 400
        assert response.json().get('error') >= 'Missing password'


def test_create_successful():
    with allure.step('Create successful'):
        response = regres.post('users', json=testUser)

        assert response.status_code == 201
        assert response.reason == 'Created'
