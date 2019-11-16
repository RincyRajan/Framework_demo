from Demo.pom.login import Login
import pytest
from selenium import webdriver

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestclassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(selfself):
        self.log_in =Login()
        print("class Label seyup of pypi org")
        yield
        print("Logging out of pypi org")

    def test_tc123_verify_login(self):

        assert self.log_in.login_to_account()
        assert self.log_in.verify_login()