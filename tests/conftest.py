import pytest
from selene import browser

from framework.demo_qa import DemoQaWithEnv


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def cookie(demoqa):
    result = demoqa.login('testuser123@mail.com', 'testuser123')
    demoqa.authorization_cookie(result)
    return demoqa.authorizationCookie


@pytest.fixture(scope='function')
def window(demoqa, cookie):
    browser.config.base_url = demoqa.demoqa.url
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open(demoqa.demoqa.url)
    browser.driver.add_cookie(cookie)
    yield browser
    browser.quit()


@pytest.fixture(scope='session')
def demoqa(env):
    return DemoQaWithEnv(env)


@pytest.fixture(scope='session')
def reqres(env):
    return DemoQaWithEnv(env).reqres
