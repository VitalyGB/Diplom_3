from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    HEADER_ORDER_FEED = (By.XPATH, "//h1[text()='Лента заказов']")

    COUNTER_ALL_TIME = (By.XPATH, "//p[contains(.,'Выполнено за все время')]/following-sibling::p")
    COUNTER_TODAY = (By.XPATH, "//p[contains(.,'Выполнено за сегодня')]/following-sibling::p")

    ORDERS_READY = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList__')][1]/li")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]/li")

    ORDER_MODAL_TITLE = (By.XPATH, "//h2[contains(@class,'Modal_modal__title__')]")
    BTN_CLOSE_ORDER_MODAL = (By.XPATH, "//button[contains(@class,'Modal_modal__close__')]")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class^='Modal_modal_overlay']")
    ORDER_MODAL_NUMBER = (By.XPATH, "//div[starts-with(@class,'Modal_modal_') "
                                    "and not(contains(@class,'overlay'))]//*[contains(@class,'text_type_digits')]") 