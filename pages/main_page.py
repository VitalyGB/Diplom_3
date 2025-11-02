import allure

from selenium.common import TimeoutException, NoSuchElementException
from locators.main_page_locators import MainPageLocators as L
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def go_to_personal_account(self):
        self.click(L.BUTTON_PERSONAL_ACCOUNT)

    @allure.step("Клик по кнопке 'Конструктор'")
    def go_to_constructor(self):
        self.click(L.BUTTON_CONSTRUCTOR)

    @allure.step("Клик по кнопке 'Лента Заказов'")
    def go_to_order_feed(self):
        self.click(L.BUTTON_ORDER_FEED) 

    @allure.step("Клик на ингредиент и ждем отображение окна с его описанием")
    def open_ingredient_details(self, ingredient_name):
        self.click(L.INGREDIENT_BY_NAME(ingredient_name))
        self.wait_visible(L.POPUP)

    @allure.step("Клик на крестик в окне с описанием ингредиента и ждем закрытия")
    def close_ingredient_details(self):
        self.click(L.BUTTON_CLOSE_POPUP)
        self.wait_invisible(L.POPUP)

    @allure.step("проверка отображаения окна с описанием ингредиента")
    def is_popup_open(self, timeout=5):
        try:
            self.wait_visible(L.INGREDIENT_MODAL, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Получение названия ингредиента в окне с его описанием")
    def get_opened_ingredient_name(self) -> str:
        return self.text_of(L.INGREDIENT_MODAL_TITLE).strip()

    @allure.step("Проверка закрытия окна с описанием ингредиента")
    def is_popup_closed(self, timeout=5):
        try:
            return self.wait_invisible(L.POPUP, timeout)
        except TimeoutException:
            return False

    @allure.step("Получаем текст в заголовке Конструктора")
    def constructor_header(self):
        return self.text_of(L.HEADER_CONSTRUCTOR)

    @allure.step("Перенос ингредиента в корзину")
    def move_ingredient_to_basket(self, ingredient_name):
        try:
            self.click(L.TAB_BUNS, timeout=2)
        except Exception:
            pass

        loc = L.INGREDIENT_BY_NAME(ingredient_name)

        for _ in range(3):
            try:
                self.scroll_into_view(loc)
                source = self.wait_visible(loc, timeout=4)
                break
            except (TimeoutException, NoSuchElementException):
                self.scroll_by(0, 400)
        else:
            raise NoSuchElementException(f"Не найден ингредиент: {ingredient_name}")

        source = self.find(loc)
        target = self.find(L.BASKET_UPPER_BUN)
        self.drag_and_drop(source, target)

    @allure.step("Получаем значение счетчика для количества добавленных ингредиентов")
    def get_ingredient_counter(self, ingredient_id: str) -> int:
        try:
            return int(self.text_of(L.INGREDIENT_COUNTER_BY_ID(ingredient_id)))
        except Exception:
            return 0

    @allure.step("Добавление ингредиента в корзину")
    def add_ingredient_to_basket(self, ingredient_name):
        self.move_ingredient_to_basket(ingredient_name)

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def place_order(self):
        self.click(L.BTN_PLACE_ORDER)