import time
import allure
from pages.order_feed_page import OrderFeedPage
from data.data import EMAIL, PASSWORD
from locators.main_page_locators import MainPageLocators

class TestOrderPage:

    @allure.feature('Лента заказов')
    @allure.story('Открытие модального окна с деталями заказа')
    @allure.title('Тест открытия модального окна с деталями заказа')
    def test_order_modal_opens(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Открываем страницу ленты заказов'):
            order_feed_page.open_feed_page()

        with allure.step('Кликаем по последнему заказу'):
            order_feed_page.click_last_order()

        with allure.step('Проверяем, что модальное окно с деталями заказа открылось'):
            content = order_feed_page.get_order_details_content()
            assert content != "", "Модальное окно с деталями заказа не открылось"

    @allure.feature('Лента заказов')
    @allure.story('Отображение заказов пользователя')
    @allure.title('Тест отображения заказов пользователя в ленте')
    def test_user_orders_displayed_in_feed(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            order_feed_page.login(EMAIL, PASSWORD)

        with allure.step('Создаем новый заказ'):
            order_feed_page.drag_and_drop_ingredient(
                MainPageLocators.INGREDIENT_R2D3_BUN,
                MainPageLocators.ORDER_TARGET_TOP
            )
            order_feed_page.click_place_an_order()

        with allure.step('Получаем идентификатор заказа'):
            order_id = order_feed_page.get_order_id_from_details()

        with allure.step('Закрываем детали заказа и открываем ленту заказов'):
            order_feed_page.click_close_order_details()
            order_feed_page.open_feed_page()

        with allure.step('Проверяем, что заказ отображается в ленте заказов'):
            assert order_feed_page.is_order_id_in_feed(order_id), \
                f"Идентификатор заказа {order_id} не найден в ленте заказов"

    @allure.feature('Лента заказов')
    @allure.story('Увеличение общего счётчика заказов')
    @allure.title('Тест увеличения общего счётчика заказов')
    def test_total_orders_counter_increases_after_new_order(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            order_feed_page.login(EMAIL, PASSWORD)

        with allure.step('Открываем ленту заказов'):
            order_feed_page.click_feed()

        with allure.step('Получаем начальный счётчик заказов'):
            initial_total_orders = order_feed_page.get_total_orders_counter()

        with allure.step('Создаем новый заказ'):
            order_feed_page.click_constructor()
            order_feed_page.drag_and_drop_ingredient(
                MainPageLocators.INGREDIENT_R2D3_BUN,
                MainPageLocators.ORDER_TARGET_TOP
            )
            order_feed_page.click_place_an_order()

        with allure.step('Ждем обновления данных'):
            time.sleep(5)

        with allure.step('Проверяем, что общий счётчик заказов увеличился'):
            order_feed_page.open_feed_page()
            updated_total_orders = order_feed_page.get_total_orders_counter()
            assert updated_total_orders > initial_total_orders, \
                f"Ожидалось увеличение счетчика. Было: {initial_total_orders}, стало: {updated_total_orders}"

    @allure.feature('Лента заказов')
    @allure.story('Увеличение счётчика заказов за сегодня')
    @allure.title('Тест увеличения счётчика заказов за сегодня')
    def test_today_orders_counter_increases_after_new_order(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            order_feed_page.login(EMAIL, PASSWORD)

        with allure.step('Открываем ленту заказов'):
            order_feed_page.click_feed()

        with allure.step('Получаем начальный счётчик заказов за сегодня'):
            initial_today_orders = order_feed_page.get_today_completed_counter()

        with allure.step('Создаем новый заказ'):
            order_feed_page.click_constructor()
            order_feed_page.drag_and_drop_ingredient(
                MainPageLocators.INGREDIENT_R2D3_BUN,
                MainPageLocators.ORDER_TARGET_TOP
            )
            order_feed_page.click_place_an_order()

        with allure.step('Закрываем детали заказа и открываем ленту заказов'):
            order_feed_page.click_close_order_details()
            order_feed_page.click_feed()

        with allure.step('Проверяем, что счётчик заказов за сегодня увеличился'):
            updated_today_orders = order_feed_page.get_today_completed_counter()
            assert updated_today_orders > initial_today_orders, \
                f"Ожидалось увеличение счетчика на 1. Было: {initial_today_orders}, стало: {updated_today_orders}"

    @allure.feature('Лента заказов')
    @allure.story('Отображение номера заказа в статусе "В работе"')
    @allure.title('Тест отображения номера заказа в разделе "В работе"')
    def test_order_number_appears_in_in_progress_after_order_placement(self, driver):
        order_feed_page = OrderFeedPage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            order_feed_page.login(EMAIL, PASSWORD)

        with allure.step('Создаем новый заказ'):
            order_feed_page.click_constructor()
            order_feed_page.drag_and_drop_ingredient(
                MainPageLocators.INGREDIENT_R2D3_BUN,
                MainPageLocators.ORDER_TARGET_TOP
            )
            order_feed_page.click_place_an_order()

        with allure.step('Получаем идентификатор заказа'):
            order_id = order_feed_page.get_order_id_from_details()

        with allure.step('Закрываем модальное окно и проверяем раздел "В работе"'):
            order_feed_page.click_close_order_details()
            order_feed_page.click_feed()

        with allure.step('Проверяем, что номер заказа появился в разделе "В работе"'):
            assert order_feed_page.is_order_number_in_progress(order_id), \
                f"Номер заказа {order_id} не появился в разделе 'В работе'"
