from session3.base.base_test import BaseTest
from session3.pages.login_page import LoginPage


class TestPom(BaseTest):
    driver = 'chrome'
    def test_pom(self):
        login = LoginPage(self.driver)
        login.enter_user_name('standard_user')
        login.enter_password('secret_sauce')
        home_page = login.click_login_button()

        name = home_page.get_product_name()
        #use the dynamic method
        home_page.click_add_to_cart("backpack")
        cart_page = home_page.click_cart_button()
        cart_name = cart_page.get_item_name()
        self.assertEqual(name, cart_name, "Product is not added to cart")
        cart_page.click_remove_item('backpack')
        self.assertTrue(cart_page.is_product_removed('backpack'))
