import pytest
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browsers_chrome(request):
    browser_count = request.param

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1024,768")
    options.add_argument('--disable-cache')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-blink-features=MetricsInterceptor')
    # options.add_argument("--headless=new")

    drivers = []

    logger.info(f'Start {browser_count} browsers')
    service = Service(executable_path=ChromeDriverManager().install())

    for _ in range(browser_count):
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_window_size(1024, 768)
        drivers.append(driver)

    yield drivers

    logger.info('Close browser')
    for driver in drivers:
        driver.close()
        driver.quit()
