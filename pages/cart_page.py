from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def compare_prices(self):
        assert self.element_is_present(*CartPageLocators.BOOK1_CART_PRICE)
