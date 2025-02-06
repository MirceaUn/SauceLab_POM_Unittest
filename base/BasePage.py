from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from TestingFramework.base.Browser import Browser
import TestingFramework.utilities.CustomLogging as cl


class BasePage(Browser):
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def open_homepage(self, typeBrowser, url):
        try:
            wd = Browser()
            self.driver = wd.get_driver(typeBrowser)
            self.driver.get(url)
            self.log.info("Web Page Launched with URL : " + url)
        except:
            self.log.info("Web Page not Launched with URL : " + url)
            assert False

    def checkPageTitle(self, title):
        try:
            assert title in self.driver.title
            self.log.info("Web Page has the title : " + title)
        except:
            self.log.error("Web Page with the title : " + title + " has not been found")
            assert False

    def find_element(self, locator):
        web_element = None
        try:
            web_element = self.driver.find_element(*locator)
            self.log.info("WebElement with " + str(locator) + " found")
        except:
            self.log.error("WebElement with " + str(locator) + " not found")
            assert False
        return web_element

    def find_elements(self, locator):
        list_web_elements = None
        try:
            list_web_elements = self.driver.find_element(*locator)
            self.log.info("WebElements with " + str(locator) + " found")
        except:
            self.log.error("WebElements with " + str(locator) + " not found")
            assert False
        return list_web_elements

    def send_text(self, locator, text):
        try:
            self.find_element(locator).send_keys(text)
            self.log.info("Sent the text: " + text + " to the locator: " + str(locator))
        except:
            self.log.error("Unable to send the text: " + text + " to the locator: " + str(locator))
            assert False

    def click_element(self, locator):
        try:
            webElement = self.waitElement(locator)
            webElement.click()
            self.log.info("Clicked on the element with the locator: " + str(locator))
        except:
            self.log.error("Unable to click on the element with the locator: " + str(locator))
            assert False

    def waitElement(self, locator):
        webElement = None
        try:
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located(locator))
            self.log.info("WebElement found with locator: " + str(locator))
        except:
            self.log.error("WebElement not found with locator: ", str(locator))
            assert False
        return webElement

    def verify_current_url(self, expected_url):
        return self.driver.current_url == expected_url

    def verify_if_element_is_displayed(self, locator):
        elementDisplayed = None
        try:
            webElement = self.waitElement(locator)
            elementDisplayed = webElement.is_displayed()
            self.log.info("WebElement with locator: " + str(locator) + " is displayed")
        except:
            self.log.error("WebElement with locator: " + str(locator) + " is not displayed")
            assert False
        return elementDisplayed

    def get_text(self, locator):
        elementText = None
        try:
            webElement = self.waitElement(locator)
            elementText = webElement.text
            self.log.info("Got the text: " + elementText + " from the WebElement with the locator: " + str(locator))
        except:
            self.log.error("Unable to get text from locator: " + str(locator))
            assert False
        return elementText
