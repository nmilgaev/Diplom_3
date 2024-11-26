from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data.data import LOGIN_URL
import time

class AccountPage(BasePage):
    def click_account_button(self):
        time.sleep(5)
        self.click_when_clickable(AccountPageLocators.ACCOUNT_BUTTON)

    def click_order_history_button(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    def click_logout_button(self):
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    def get_login_button_text_after_logout(self):
        return self.get_text_from_element(AccountPageLocators.LOGIN_AFTER_LOGOUT)


    def open_login_page(self):
        self.driver.get(LOGIN_URL)

    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(AccountPageLocators.EMAIL_INPUT, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_INPUT, password)
        time.sleep(5)
        self.click_to_element(AccountPageLocators.LOGIN_BUTTON)