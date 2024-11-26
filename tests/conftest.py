import pytest  # Обязательно импортируем pytest
from selenium import webdriver

class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

# Эта функция добавляет возможность передачи параметра --browser в командной строке pytest
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Выбор браузера: 'chrome' или 'firefox'."
    )

@pytest.fixture
def driver(request):
    # Получаем параметр браузера из командной строки
    browser_name = request.config.getoption("--browser")
    # Создаем и возвращаем соответствующий драйвер
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()  # Открытие окна на весь экран
    yield driver
    driver.quit()
