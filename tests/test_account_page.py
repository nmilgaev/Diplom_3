import allure
from data.data import EMAIL, PASSWORD
from pages.account_page import AccountPage


@allure.feature('Личный кабинет')
@allure.story('Тесты функционала личного кабинета')
class TestAccountPage:

    @allure.title('Тест перехода в личный кабинет')
    def test_click_account_button(self, driver):
        account_page = AccountPage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            account_page.click_account_button()

        with allure.step('Проверяем, что кнопка "Выход" отображается'):
            assert account_page.is_logout_button_visible(), \
                "Не удалось войти в личный кабинет"

    @allure.title('Тест перехода в историю заказов')
    def test_click_order_history(self, driver):
        account_page = AccountPage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            account_page.click_account_button()

        with allure.step('Переходим в раздел "История заказов"'):
            account_page.click_order_history_button()

        with allure.step('Проверяем, что заказ выполнен'):
            assert account_page.is_order_completed(), \
                "Не удалось перейти в историю заказов"

    @allure.title('Тест выхода из аккаунта')
    def test_logout(self, driver):
        account_page = AccountPage(driver)

        with allure.step('Выполняем вход в аккаунт'):
            account_page.login(EMAIL, PASSWORD)

        with allure.step('Нажимаем на кнопку "Личный кабинет"'):
            account_page.click_account_button()

        with allure.step('Нажимаем на кнопку "Выход"'):
            account_page.click_logout_button()

        with allure.step('Проверяем, что кнопка "Вход" отображается после выхода'):
            assert account_page.is_login_button_visible_after_logout(), \
                "Не удалось выйти из аккаунта"
