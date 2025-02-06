from selenium import webdriver
import TestingFramework.utilities.CustomLogging as cl

class Browser:
    log = cl.customLogger()

    def __init__(self):
        self.driver = None

    def get_driver(self, browserName):
        if self.driver is None:
            if browserName == 'chrome':
                self.driver = webdriver.Chrome()
                self.log.info("Chrome Driver is initializing")
            elif browserName == 'firefox':
                self.driver = webdriver.Firefox()
                self.log.info("FireFox Driver is initializing")

            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
