import allure

from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получаем текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url

    @allure.step("Ожидаем видимость элемента")
    def wait_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидаем кликабельность элемента")
    def wait_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидаем, пока элемент исчезнет")
    def wait_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Кликаем на элемент")
    def click(self, locator, timeout=10):
        el = self.wait_clickable(locator, timeout)
        try:
            el.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", el)

    @allure.step("Кликаем на элемент при помощи JS")
    def js_click(self, locator):
        el = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", el)

    @allure.step("Получаем текст элемента")
    def text_of(self, locator, timeout=10):
        return self.wait_visible(locator, timeout).text

    @allure.step("Перетаскиваем элемент")
    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("Скроллим до элемента")
    def scroll_into_view(self, locator):
        el = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        return el

    @allure.step("Ждем выполнение условия")
    def wait_until(self, condition, timeout=10, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency).until(condition)

    @allure.step("Ищем элемент")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Ищем список элементов")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Скроллим страницу по горизонтали и по вертикали")
    def scroll_by(self, x=0, y=400):
        self.driver.execute_script(f"window.scrollBy({x}, {y});") 