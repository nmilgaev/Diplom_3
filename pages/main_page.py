from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from selenium.common.exceptions import NoSuchElementException
from locators.main_page_locators import MainPageLocators
from data.data import LOGIN_URL

class MainPage(BasePage):
    def click_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_place_an_order(self):
        self.click_to_element(MainPageLocators.PLACE_AN_ORDER)

    def is_burger_constructor_visible(self):
        return self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_SECTION).is_displayed()

    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    def is_order_feed_counter_visible(self):
        return self.find_element_with_wait(MainPageLocators.COMPLETED_ORDERS).is_displayed()

    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_R2D3_BUN)

    def is_ingredient_details_visible(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS_TITLE).is_displayed()

    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    def add_ingredient_to_order(self):
        self.click_to_element(MainPageLocators.ADD_INGREDIENT_BUTTON)

    def get_ingredient_counter(self):
        """Возвращает текущее значение каунтера для ингредиента."""
        return int(self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER))

    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(AccountPageLocators.EMAIL_INPUT, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_INPUT, password)
        self.click_to_element(AccountPageLocators.LOGIN_BUTTON)

    def open_login_page(self):
        self.driver.get(LOGIN_URL)

    def is_ingredient_details_visible(self):
        try:
            element = self.driver.find_element(*MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def drag_and_drop_ingredient(self, ingredient_locator, target_locator):
        """
        Перетаскивание ингредиента в зону заказа с использованием JavaScript для стабильности в Firefox.
        :param ingredient_locator: Локатор ингредиента, который перетаскивается.
        :param target_locator: Локатор зоны, куда перетаскивается ингредиент.
        """
        self.find_element_with_wait(ingredient_locator)
        self.find_element_with_wait(target_locator)

        element_from = self.driver.find_element(*ingredient_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    def get_order_success_message(self):
        return self.get_text_from_element(MainPageLocators.ORDER_SUCCESS_MESSAGE)
