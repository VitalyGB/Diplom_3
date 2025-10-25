from selenium.webdriver.common.by import By

class MainPageLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    BUTTON_ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    TAB_BUNS = (By.XPATH, "//span[normalize-space(.)='Булки']")

    HEADER_CONSTRUCTOR = (By.XPATH, "//h1[text()='Соберите бургер']")

    POPUP = (By.CLASS_NAME, "Modal_modal__contentBox__sCy8X")
    BUTTON_CLOSE_POPUP = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]")

    INGREDIENT_COUNTER_BY_ID = lambda _id: (
        By.XPATH,
        f"//a[contains(@href,'/ingredient/{_id}')]//p[contains(@class,'counter_counter__')]",
    )

    INGREDIENT_MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal__')]") 
    INGREDIENT_MODAL_OPENED = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//p[contains(@class,'text_type_main-medium')]")

    BASKET_UPPER_BUN = (By.XPATH, "//span[contains(text(),'Перетяните булочку сюда')]")

    BTN_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

    @staticmethod
    def INGREDIENT_BY_NAME(name: str):
        return By.XPATH, f"//img[contains(@alt, '{name}')] | //p[normalize-space(text())='{name}']"