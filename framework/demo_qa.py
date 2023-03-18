from config import Hosts
from utils.base_session import BaseSession


class DemoQaWithEnv:
    authorizationCookie = None

    def __init__(self, env):
        self.demoqa = BaseSession(url=Hosts(env).demoqa)
        self.reqres = BaseSession(url=Hosts(env).reqres)
        self.authorizationCookie = None

    def login(self, email, password):
        return self.demoqa.post(
            url="/login",
            params={'Email': email, 'Password': password},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )

    def authorization_cookie(self, response):
        self.authorizationCookie = {"name": "NOPCOMMERCE.AUTH", "value": response.cookies.get("NOPCOMMERCE.AUTH")}
