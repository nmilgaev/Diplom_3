import allure
from pages.main_page import MainPage
from data.data import EMAIL, PASSWORD
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.feature('Основной функционал')
    @allure.story('Переход по клику на «Конструктор»')
    @allure.title('Тест перехода в конструктор')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Проверяем, что секция "Собери бургер" отображается'):
            assert main_page.is_burger_constructor_visible(), "Секция 'Собери бургер' не отображается!"

    @allure.feature('Основной функционал')
    @allure.story('Переход по клику на «Лента заказов»')
    @allure.title('Тест перехода в ленту заказов')
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.open_login_page()

        with allure.step('Нажимаем на "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Проверяем, что счетчик выполненных заказов отображается'):
            assert main_page.is_order_feed_counter_visible(), "Счетчик выполненных заказов не отображается!"

    @allure.feature('Основной функционал')
    @allure.story('Проверка деталей ингредиента')
    @allure.title('Тест отображения деталей ингредиента')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Нажимаем на ингредиент'):
            main_page.click_ingredient()

        with allure.step('Проверяем, что окно с деталями ингредиента отображается'):
            assert main_page.is_ingredient_details_visible(), "Детали ингредиента не отображаются!"

    @allure.feature('Основной функционал')
    @allure.story('Закрытие всплывающего окна с деталями ингредиента')
    @allure.title('Тест закрытия окна деталей ингредиента')
    def test_close_details(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Нажимаем на ингредиент'):
            main_page.click_ingredient()

        with allure.step('Закрываем окно с деталями ингредиента'):
            main_page.close_ingredient_details()

        with allure.step('Проверяем, что окно с деталями ингредиента закрыто'):
            assert not main_page.is_ingredient_details_visible()

    @allure.feature('Основной функционал')
    @allure.story('Проверка увеличения каунтера ингредиентов')
    @allure.title('Тест увеличения каунтера ингредиентов')
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Получаем начальное значение каунтера ингредиентов'):
            initial_counter = main_page.get_ingredient_counter()

        with allure.step('Добавляем ингредиент в заказ'):
            main_page.drag_and_drop_ingredient(
                MainPageLocators.INGREDIENT_R2D3_BUN,
                MainPageLocators.ORDER_TARGET_TOP
            )

        with allure.step('Проверяем, что каунтер увеличился'):
            updated_counter = main_page.get_ingredient_counter()

        assert updated_counter == initial_counter + 2, \
            f"Каунтер не увеличился! Ожидалось: {initial_counter + 2}, но получено: {updated_counter}"

    @allure.feature('Основной функционал')
    @allure.story('Оформление заказа для залогиненного пользователя')
    @allure.title('Тест оформления заказа для залогиненного пользователя')
    def test_order_creation_for_logged_in_user(self, driver):
        main_page = MainPage(driver)

        with allure.step('Открываем страницу входа'):
            main_page.open_login_page()

        with allure.step('Выполняем вход в аккаунт'):
            main_page.login(EMAIL, PASSWORD)

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Добавляем ингредиент в заказ'):
            main_page.drag_and_drop_ingredient(
                MainPageLocators.INGREDIENT_R2D3_BUN,
                MainPageLocators.ORDER_TARGET_TOP
            )

        with allure.step('Оформляем заказ'):
            main_page.click_place_an_order()

        with allure.step('Проверяем, что отображается сообщение об успешном заказе'):
            success_message = main_page.get_order_success_message()
            assert success_message == "Ваш заказ начали готовить", \
                f"Ожидалось сообщение: 'Ваш заказ начали готовить', но получено: {success_message}"
