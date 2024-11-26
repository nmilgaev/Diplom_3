from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locator(self, locator, num):
        method, locator_str = locator
        locator_str = locator_str.format(num)
        return method, locator_str

    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def click_when_clickable(self, locator):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()


