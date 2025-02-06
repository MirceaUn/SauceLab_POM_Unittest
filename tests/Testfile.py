import time

from selenium.webdriver.common.by import By

from TestingFramework.base.Browser import Browser
import TestingFramework.utilities.CustomLogging as cl
from TestingFramework.base.BasePage import BasePage


wd = Browser()
bp = BasePage()

LOGIN_EMAIL_FIELD = (By.ID, "user-name")
LOGIN_PASSWORD_FIELD = (By.ID, "password")
LOGIN_ACCOUNT_BUTTON = (By.ID, "login-button")
SHOPPING_CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')

bp.open_homepage('chrome','https://www.saucedemo.com/')
bp.send_text(LOGIN_EMAIL_FIELD,"standard_user")
bp.send_text(LOGIN_PASSWORD_FIELD, "secret_sauce")
bp.click_element(LOGIN_ACCOUNT_BUTTON)
bp.verify_current_url("https://www.saucedemo.com/inventory.html")
bp.verify_if_element_is_displayed(SHOPPING_CART_BUTTON)

time.sleep(3)
wd.close_driver()
