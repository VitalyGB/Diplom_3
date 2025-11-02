import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from helpers.data import TestData, Credentials
from pages.login_page import LoginPage

@allure.feature("Лента заказов Stellar Burgers")
class TestOrderFeed:
    @allure.title("Счетчик 'Выполнено за все время' увеличивается после заказа")
    def test_all_time_counter_increases(self, driver):
        main = MainPage(driver)
        order = OrderFeedPage(driver)
        login = LoginPage(driver)
        with allure.step("Переход в 'Личный кабинет'"):
            main.go_to_personal_account()
        with allure.step("Авторизация"):
            login.login(Credentials.email, Credentials.password)
        with allure.step("Переход на страницу 'Лента заказов' и получение значения счетчика 'Выполнено за все время'"):
            main.go_to_order_feed()
            initial_count = order.all_time_counter()
        with allure.step("Переход на страницу 'Конструктор' и создаем заказ"):
            main.go_to_constructor()
            main.add_ingredient_to_basket(TestData.ingredient_name)
            main.place_order()
            order.close_order_modal()
        with allure.step("Открываем 'Ленту заказов' повторно и получаем новое значение счетчика"):
            main.go_to_order_feed()
            current_count = order.all_time_counter()
        with allure.step("Проверяем, что значение счетчика увеличилось"):
            assert current_count > initial_count

    @allure.title("Счетчик 'Выполнено за сегодня' увеличивается после заказа")
    def test_today_counter_increases(self, driver):
        main = MainPage(driver)
        order = OrderFeedPage(driver)
        login = LoginPage(driver)
        with allure.step("Переход в 'Личный кабинет'"):
            main.go_to_personal_account()
        with allure.step("Авторизация"):
            login.login(Credentials.email, Credentials.password)
        with allure.step("Переход на страницу 'Лента заказов' и получаем значение счётчика 'Выполнено за сегодня'"):
            main.go_to_order_feed()
            initial_count = order.today_counter()
        with allure.step("Переход на страницу 'Конструктор' и создаем заказ"):
            main.go_to_constructor()
            main.add_ingredient_to_basket(TestData.ingredient_name)
            main.place_order()
            order.close_order_modal()
        with allure.step("Открываем 'Ленту заказов' повторно и получаем новое значение счетчика"):
            main.go_to_order_feed()
            current_count = order.today_counter()
        with allure.step("Проверяем, что значение счетчика увеличилось"):
            assert current_count > initial_count

    @allure.title("Номер нового заказа появляется в разделе 'В работе'")
    def test_order_number_in_progress(self, driver):
        main = MainPage(driver)
        order = OrderFeedPage(driver)
        login = LoginPage(driver)
        with allure.step("Переход в 'Личный кабинет'"):
            main.go_to_personal_account()
        with allure.step("Авторизация"):
            login.login(Credentials.email, Credentials.password)
        with allure.step(f"Создание заказ с ингредиентом '{TestData.ingredient_name}'"):
            main.add_ingredient_to_basket(TestData.ingredient_name)
            main.place_order()
        with allure.step("Получение номера заказа из всплывающего окна"):
            order_number = order.order_number_from_modal()
        with allure.step("Закрытие всплывающего окна"):
            order.close_order_modal()
        with allure.step("Переход на страницу 'Лента заказов'"):
            main.go_to_order_feed()
        with allure.step(f"Проверяем, что заказ с номером {order_number} отображается в разделе 'В работе'"):
            assert order.is_order_in_progress(order_number) 