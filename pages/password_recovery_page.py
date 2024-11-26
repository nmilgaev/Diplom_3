from .base_page import BasePage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from data.data import LOGIN_URL
from locators.account_page_locators import AccountPageLocators
class PasswordRecoveryPage(BasePage):
    def open_login_page(self):
        self.driver.get(LOGIN_URL)
    def navigate_to_password_recovery_page(self):
        self.click_to_element(PasswordRecoveryPageLocators.RECOVER_PASSWORD_BUTTON)

    def enter_email(self, email):
        self.add_text_to_element(AccountPageLocators.EMAIL_INPUT, email)

    def click_recover_button(self):
        self.click_to_element(PasswordRecoveryPageLocators.RECOVER_BUTTON)

    def toggle_password_visibility(self):
        self.click_to_element(PasswordRecoveryPageLocators.TOGGLE_PASSWORD_BUTTON)

    def get_password_input_type(self):
        return self.find_element_with_wait(PasswordRecoveryPageLocators.NEW_PASSWORD_INPUT).get_attribute("type")
