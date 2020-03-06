from pages.base_page import BasePage
from pages.locators import ProductPageLocatots


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocatots.BASKET_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def is_rigth_product_in_basket(self):
        element = self.browser.find_element(*ProductPageLocatots.PRODUCT_NAME)
        product_name = element.text
        element = self.browser.find_element(*ProductPageLocatots.PRODUCT_IN_BASKET)
        product_in_basket = element.text
        assert product_name == product_in_basket, \
            f'Added {product_in_basket}, but should be {product_name}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocatots.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def message_disappeared_after_adding(self):
        assert self.is_disappeared(*ProductPageLocatots.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
