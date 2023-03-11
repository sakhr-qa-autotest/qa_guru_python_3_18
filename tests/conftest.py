import pytest
from selene import browser

from config import Hosts
from utils.base_session import BaseSession


def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="prod")


def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def window(request):
    hosts = Hosts(env(request))
    browser.config.base_url = hosts.demoqa
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open(hosts.demoqa)
    return browser


@pytest.fixture(scope='session')
def demoqa(request):
    hosts = Hosts(env(request))
    return BaseSession(hosts.demoqa)


@pytest.fixture(scope='session')
def reqres(request):
    hosts = Hosts(env(request))
    return BaseSession(hosts.reqres)
