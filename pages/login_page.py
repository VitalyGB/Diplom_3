import allure

from locators.login_page_locators import LoginPageLocators as L
from pages.base_page import BasePage

class LoginPage(BasePage):
    @allure.step("Авторизация")
    def login(self, email, password):
        self.wait_visible(L.INPUT_EMAIL).send_keys(email)
        self.wait_visible(L.INPUT_PASSWORD).send_keys(password)
        self.click(L.BUTTON_SUBMIT_LOGIN) 