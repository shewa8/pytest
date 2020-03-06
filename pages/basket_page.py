from pages.base_page import BasePage
from pages.locators import MainPageLocators
from pages.locators import ProductPageLocatots


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        element = self.browser.find_element(*MainPageLocators.EMPTY_BASKET)
        is_basket_empty = element.text
        assert is_basket_empty == "Your basket is empty. Continue shopping", \
            "Basket is NOT empty"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocatots.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)
