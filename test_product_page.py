import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage


def test_guest_can_add_product_to_basket_first_test(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.is_rigth_product_in_basket()


offer_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


@pytest.mark.need_review
@pytest.mark.parametrize('link', offer_number)
def test_guest_can_add_product_to_basket(browser, link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.is_rigth_product_in_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.message_disappeared_after_adding()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_empty_basket()
    page.should_not_be_success_message()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = ProductPage(browser, link)
        page.open()
        register_page = LoginPage(browser, browser.current_url)
        register_page.register_new_user()
        register_page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()
        page.is_rigth_product_in_basket()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
