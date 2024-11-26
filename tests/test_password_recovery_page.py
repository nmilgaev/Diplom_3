import allure
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.password_recovery_page import PasswordRecoveryPage
from data.data import EMAIL

class TestPasswordRecoveryPage:

    @allure.feature('Восстановление пароля')
    @allure.story('Переход на страницу восстановления пароля')
    @allure.title('Тест перехода на страницу восстановления пароля')
    def test_navigate_to_password_recovery_page(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)

        with allure.step('Открываем страницу авторизации'):
            password_recovery_page.open_login_page()

        with allure.step('Переходим на страницу восстановления пароля'):
            password_recovery_page.navigate_to_password_recovery_page()

        with allure.step('Проверяем, что кнопка "Восстановить" доступна'):
            assert password_recovery_page.find_element_with_wait(PasswordRecoveryPageLocators.RECOVER_BUTTON), \
                "Не удалось попасть на страницу восстановления пароля"

    @allure.feature('Восстановление пароля')
    @allure.story('Процесс восстановления пароля')
    @allure.title('Тест процесса восстановления пароля')
    def test_password_recovery(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)

        with allure.step('Открываем страницу авторизации'):
            password_recovery_page.open_login_page()

        with allure.step('Переходим на страницу восстановления пароля'):
            password_recovery_page.navigate_to_password_recovery_page()

        with allure.step('Вводим email для восстановления'):
            password_recovery_page.enter_email(EMAIL)

        with allure.step('Нажимаем кнопку восстановления'):
            password_recovery_page.click_recover_button()

        with allure.step('Проверяем, что поле для ввода нового пароля появилось'):
            assert password_recovery_page.find_element_with_wait(PasswordRecoveryPageLocators.NEW_PASSWORD_INPUT), \
                "Не удалось перейти к вводу нового пароля"

    @allure.feature('Восстановление пароля')
    @allure.story('Переключение видимости пароля')
    @allure.title('Тест переключения видимости пароля')
    def test_toggle_password_visibility(self, driver):
        password_recovery_page = PasswordRecoveryPage(driver)

        with allure.step('Открываем страницу авторизации'):
            password_recovery_page.open_login_page()

        with allure.step('Переходим на страницу восстановления пароля'):
            password_recovery_page.navigate_to_password_recovery_page()

        with allure.step('Вводим email для восстановления'):
            password_recovery_page.enter_email(EMAIL)

        with allure.step('Нажимаем кнопку восстановления'):
            password_recovery_page.click_recover_button()

        with allure.step('Переключаем видимость пароля'):
            password_recovery_page.toggle_password_visibility()

        with allure.step('Проверяем, что поле пароля стало активным '):
            updated_type = password_recovery_page.get_password_input_type()
            assert updated_type == "text", "Поле пароля должно стать активным"
