import allure
import re

from selenium.common import TimeoutException
from locators.order_feed_page_locators import OrderFeedPageLocators as L
from pages.base_page import BasePage

class OrderFeedPage(BasePage):

    @allure.step("Ожидание загрузки ленты заказов")
    def wait_order_feed_loaded(self):
        self.wait_visible(L.HEADER_ORDER_FEED)

    @allure.step("Получение текста заголовка ленты заказов")
    def order_feed_header(self):
        return self.text_of(L.HEADER_ORDER_FEED)

    @allure.step("Получение значения счетчика 'Выполнено за все время'")
    def all_time_counter(self, timeout=10):
        self.wait_order_feed_loaded()
        return int(self.text_of(L.COUNTER_ALL_TIME, timeout))

    @allure.step("Получение значения счетчика 'Выполнено за сегодня'")
    def today_counter(self, timeout=10):
        self.wait_order_feed_loaded()
        return int(self.text_of(L.COUNTER_TODAY, timeout))

    @allure.step("Получение номера заказа из окна с его идентификатором")
    def order_number_from_modal(self, timeout=20):
        def _real_order_number(driver):
            try:
                txt = self.text_of(L.ORDER_MODAL_NUMBER, 1).strip()
            except Exception:
                return False
            if re.fullmatch(r"\d{5,}", txt) and txt != "9999":
                return txt
            return False

        return self.wait_until(_real_order_number, timeout, poll_frequency=0.5)

    @allure.step("Закрытие окна с идентификатором заказа")
    def close_order_modal(self, timeout=10):
        try:
            self.wait_visible(L.MODAL_OVERLAY, timeout)
        except TimeoutException:
            try:
                self.click(L.BTN_CLOSE_ORDER_MODAL, timeout=3)
            finally:
                return
        try:
            self.click(L.MODAL_OVERLAY, timeout=3)
        except Exception:
            try:
                self.click(L.BTN_CLOSE_ORDER_MODAL, timeout=3)
            except Exception:
                self.js_click(L.BTN_CLOSE_ORDER_MODAL)
        self.wait_invisible(L.MODAL_OVERLAY, timeout=10)

    @allure.step("Проверка отображения номера оформленного заказа в разделе 'В работе'")
    def is_order_in_progress(self, number, timeout = 20) -> bool:
        return self.wait_until(
            lambda d: any(
                o.text.endswith(str(number))
                for o in self.find_all(L.ORDERS_IN_PROGRESS)
            ),
            timeout
        ) 