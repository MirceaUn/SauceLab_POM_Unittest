from selenium.webdriver.common.by import By

from TestingFramework.base.BasePage import BasePage


class LoginPage(BasePage):

    LOGIN_EMAIL_FIELD = (By.ID, "user-name")
    LOGIN_PASSWORD_FIELD = (By.ID, "password")
    LOGIN_ACCOUNT_BUTTON = (By.ID, "login-button")
    SHOPPING_CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
    ERROR_LOGIN_MESSAGE = (By.CLASS_NAME, "h3[data-test='error']")

    def open_check_homepage(self, browser, url, title):
        self.open_homepage(browser, url)
        self.checkPageTitle(title)

    def fill_login(self, username, password):
        self.send_text(self.LOGIN_EMAIL_FIELD, username)
        self.send_text(self.LOGIN_PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_ACCOUNT_BUTTON)

    def successful_login(self, url, title):
        assert self.verify_current_url(url)
        self.checkPageTitle(title)

    def loginErrorMessage(self, errorText):
        error_message = self.get_text(self.ERROR_LOGIN_MESSAGE)
        self.verify_if_element_is_displayed(error_message)
        assert error_message == errorText
