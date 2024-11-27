from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # Поле ввода почты

    # Кнопка "Восстановить пароль"
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")

    # Поле ввода почты
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")

    # Кнопка "Восстановить"
    RECOVER_BUTTON = (By.XPATH,
                      "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    # Поле "Введите новый пароль"
    NEW_PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")

    # Кнопка "Показать/скрыть пароль" делает поле активным
    TOGGLE_PASSWORD_BUTTON = (By.XPATH, "//*[name()='path' and contains(@d,'M12 4C14.0')]")