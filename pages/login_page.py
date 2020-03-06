from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM), \
            "Register form is not presented"

    def register_new_user(self):
        element = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        element.send_keys(str(time.time()) + "@fakemail.org")
        element = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        element.send_keys("csrfmiddlewaretoken")
        element = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        element.send_keys("csrfmiddlewaretoken")
        element = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        element.click()
