import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    driver = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = self.get_driver(self.driver)
        self.driver.get('https://www.saucedemo.com/')
        self.driver.maximize_window()

    def get_driver(self, driver):
        if driver == 'chrome':
            self.driver = webdriver.Chrome()
        elif driver == 'safari':
            self.driver = webdriver.Safari()
        elif driver == 'firefox':
            self.driver = webdriver.Firefox()
        return self.driver
