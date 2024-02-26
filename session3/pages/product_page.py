from selenium.webdriver.common.by import By
from session3.base.base_page import BasePage


class ProductPage(BasePage):

    add_to_cart = 'add-to-cart-{}'
    add_to_cart_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    product_title = (By.CSS_SELECTOR, '.inventory_details_name')
    product_price = (By.CSS_SELECTOR, '.inventory_details_price')
    back_button = (By.CSS_SELECTOR, '#back-to-products')

    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart(self, product_name):
        self.driver.find_element(By.ID, self.add_to_cart.format(product_name)).click()

    def get_product_title(self):
        return self.driver.find_element(*self.product_title).text

    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text

    def click_back_button(self):
        self.driver.find_element(*self.back_button).click()
