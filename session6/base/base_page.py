from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object): #Facade class to be used by all page objects

    def __init__(self, driver, explicit_wait=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, explicit_wait)

    def driver(self):
        return self.driver

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_clickable(self, locator):
        try:
            self.wait.until(ec.element_to_be_clickable(locator))
            return True
        except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException,
                StaleElementReferenceException):
            return False
