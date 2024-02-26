from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from session3.base.base_page import BasePage
from session3.pages.cart_page import CartPage
from session3.pages.product_page import ProductPage


class HomePage(BasePage):

    add_to_cart_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    add_to_cart_bike = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    add_to_cart_shirt = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
    add_to_cart = 'add-to-cart-sauce-labs-{}'
    product = "//div[@class='inventory_item_name' and contains(text(), '{}')]"
    cart_button = (By.ID, 'shopping_cart_container')
    product_name = (By.CLASS_NAME, 'inventory_item_name')

    def __init__(self, driver):
        super().__init__(driver)
        self.wait_page_load()

    def wait_page_load(self):
        self.wait.until(ec.visibility_of_element_located(self.cart_button))

    #her bir ürün için ayrı ayrı tıklama methodları:
    def click_add_to_cart_backpack(self):
        self.driver.find_element(*self.add_to_cart_backpack).click()

    def click_add_to_cart_bike(self):
        self.driver.find_element(*self.add_to_cart_bike).click()

    #ürün locatorları ortak olduğu için duplicate methodlar yerine, tek bir method ile tıklama işlemi yapılabilir:

    def click_product(self, product_name):
        self.driver.find_element(By.XPATH, self.product.format(product_name)).click()
        return ProductPage(self.driver)

    def click_cart_button(self):
        self.driver.find_element(*self.cart_button).click()
        return CartPage(self.driver)

    def get_product_name(self):
        return self.driver.find_elements(*self.product_name)[0].text
