from datetime import datetime

from loguru import logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SHORT_TIMEOUT = 5
MEDIUM_TIMEOUT = 10
LONG_TIMEOUT = 30


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        logger.info(f"Navigate to site {url}")
        self.driver.get(url)
        logger.info(f"Current url is {self.driver.current_url}")

    def refresh_page(self):
        self.driver.refresh()

    def find_element_visible(self, locator, time=MEDIUM_TIMEOUT):
        return WebDriverWait(
            self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find visible element by locator {locator}")

    def element_invisible(self, locator, time=MEDIUM_TIMEOUT):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element(locator),
            message=f"Element located by {locator} is still visible after {time} seconds"
        )

    def find_all_elements(self, locator, time=MEDIUM_TIMEOUT):
        try:
            return WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}")
        except TimeoutException as e:
            logger.error("[{}] Element did not load. ".format(str(datetime.now())) + str(e))
            return None

    def execute_scroll_into_view(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def confirmation_alert_confirm(self) -> str:
        alert = WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.alert_is_present(),
            message="Alert not found within the given time"
        )
        alert_text = alert.text
        alert.accept()

        return alert_text

    def confirmation_alert_dismiss(self) -> str:
        alert = WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.alert_is_present(),
            message="Alert not found within the given time"
        )
        alert_text = alert.text
        alert.dismiss()

        return alert_text
