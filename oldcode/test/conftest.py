import pytest
from selenium import webdriver

@pytest.yield_fixture()

def setUp():
    print("Running method level setup")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimesetUp(browser):
    print("Running one time setUp")
    if browser == 'firefox':
        print("Running tests on FF")
    else:
        print("Running tests on chrome")
    yield
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.etoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

