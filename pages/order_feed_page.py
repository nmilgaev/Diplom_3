from .base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from data.data import LOGIN_URL, FEED_URL
from locators.account_page_locators import AccountPageLocators
import time
from locators.main_page_locators import MainPageLocators

class OrderFeedPage(BasePage):
    def click_last_order(self):
        self.click_to_element(OrderFeedPageLocators.LAST_ORDER)

    def get_order_details_content(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_DETAILS_CONTENT)

    def get_total_orders_counter(self):
        return int(self.get_text_from_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER))

    def get_today_completed_counter(self):
        self.scroll_to_element(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)
        element = self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip())

    def open_login_page(self):
        self.driver.get(LOGIN_URL)

    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(AccountPageLocators.EMAIL_INPUT, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_INPUT, password)
        self.click_to_element(AccountPageLocators.LOGIN_BUTTON)

    def open_feed_page(self):
        self.driver.get(FEED_URL)

    def click_constructor(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_feed(self):
        time.sleep(5)
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

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

    def click_place_an_order(self):
        self.click_to_element(MainPageLocators.PLACE_AN_ORDER)
        time.sleep(5)

    def click_account_button(self):
        time.sleep(5)
        self.click_when_clickable(AccountPageLocators.ACCOUNT_BUTTON)

    def click_order_history_button(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    def click_close_order_details(self):
        self.click_to_element(OrderFeedPageLocators.CLOSE_ORDER_DETAILS_BUTTON)

    def get_order_id_from_details(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_ID)

    def is_order_id_in_feed(self, order_id):
        formatted_id = f"{int(order_id):07d}"  # Добавляем нули до длины 7
        order_locator = OrderFeedPageLocators.ORDER_ID_IN_FEED
        order_locator = (order_locator[0], order_locator[1].format(formatted_id))
        return self.find_element_with_wait(order_locator)

    def is_order_number_in_progress(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        order_locator = OrderFeedPageLocators.ORDER_IN_PROGRESS_LOCATOR
        order_locator = self.format_locator(order_locator, formatted_id)

        self.find_element_with_wait(order_locator)

        return True