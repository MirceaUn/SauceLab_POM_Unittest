import unittest
from TestingFramework.pages.LoginPage import LoginPage


class LoginTests(LoginPage, unittest.TestCase):

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.driver = webdriver

    def setUpClass(self) -> None:
        self.open_check_homepage('chrome', 'https://www.saucedemo.com/', 'Swag Labs')

    def tearDown(self) -> None:
        self.close_driver()

    def test_SuccessfulLogin(self):
        self.fill_login('standard_user', 'secret_sauce')
        self.successful_login('https://www.saucedemo.com/inventory.html', 'Swag Labs')

    def test_BadCredentialsLogin(self):
        self.fill_login('standard_use', 'secret_sauc')
        self.loginErrorMessage('Epic sadface: Username and password do not match any user in this service')

