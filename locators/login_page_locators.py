from selenium.webdriver.common.by import By

class LoginPageLocators:
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    INPUT_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    BUTTON_SUBMIT_LOGIN = (By.XPATH, "//button[text()='Войти']") 