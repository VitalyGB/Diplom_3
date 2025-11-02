import allure

from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from helpers.data import TestData
from helpers.curl import *

@allure.feature("Основная функциональность Stellar Burgers")
class TestMainPage:
    @allure.title("Переходим по клику на 'Конструктор'")
    def test_click_move_to_constructor(self, driver):
        main = MainPage(driver)
        with allure.step("Кликаем на 'Личный кабинет' и переходим в раздел"):
            main.go_to_personal_account()
        with allure.step("Кликаем на 'Конструктор' и переходим в раздел"):
            main.go_to_constructor()
        with allure.step("Проверяем соответствие заголовка в разделе 'Соберите бургер'"):
            assert main.constructor_header() == "Соберите бургер"
        with allure.step("Проверяем, что URL соответствует главной странице сайта"):
            assert main.get_current_url() == main_site

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_click_move_to_order_feed(self, driver):
        main = MainPage(driver)
        order = OrderFeedPage(driver)
        with allure.step("Кликаем на 'Лента заказов'"):
            main.go_to_order_feed()
        with allure.step("Ожидаем загрузку 'Лента заказов'"):
            order.wait_order_feed_loaded()
        with allure.step("Проверяем заголовок"):
            assert order.order_feed_header() == "Лента заказов"
        with allure.step("Проверяем, что URL соответствует странице 'Лента заказов'"):
            assert main.get_current_url() == order_feed

    @allure.title("Открытие попапа с деталями ингредиента по клику")
    def test_click_to_ingredient_opens_pop_up(self, driver):
        main = MainPage(driver)
        with allure.step(f"Открываем ингредиент '{TestData.ingredient_name}'"):
            main.open_ingredient_details(TestData.ingredient_name)
        with allure.step("Проверяем, что попап открылся"):
            assert main.is_popup_open()
        with allure.step("Проверяем, что открылся попап с нужным ингредиентом"):
                assert main.get_opened_ingredient_name() == TestData.ingredient_name

    @allure.title("Закрытие попапа с деталями ингредиента по крестику")
    def test_close_ingredient_pop_up_with_cross(self, driver):
        main = MainPage(driver)
        with allure.step(f"Открываем ингредиент '{TestData.ingredient_name}'"):
            main.open_ingredient_details(TestData.ingredient_name)
        with allure.step("Закрываем попап"):
            main.close_ingredient_details()
        with allure.step("Проверяем, что попап закрылся"):
            assert main.is_popup_closed()

    @allure.title("Счетчик ингредиента увеличивается после добавления в заказ")
    def test_ingredient_counter_increases(self, driver):
        main = MainPage(driver)
        with allure.step("Получаем исходное значение счетчика"):
            initial_count = main.get_ingredient_counter(TestData.ingredient_id)
        with allure.step("Перетаскиваем булочку в корзину"):
            main.move_ingredient_to_basket(TestData.ingredient_name)
        with allure.step("Получаем новое значение счетчика"):
            current_count = main.get_ingredient_counter(TestData.ingredient_id)
        assert current_count == initial_count + 2 