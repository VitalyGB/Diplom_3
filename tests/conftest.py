import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import helpers.curl

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    headless = request.config.getoption("--headless")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1400,900")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.set_window_size(1400, 900)
    else:
        raise pytest.UsageError("--browser_name должен быть chrome или firefox")
    yield driver
    driver.quit()
