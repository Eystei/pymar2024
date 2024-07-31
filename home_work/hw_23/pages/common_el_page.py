from selenium.webdriver.common.by import By

from home_work.hw_23.pages._base_page import BasePage


class CommonElementsLocators:
    LOCATOR_PAGE_TITLE = (By.XPATH, '//h1[text()="{header}"]')

    LOCATOR_BTN_LOGOUT = (By.XPATH, '//button[@id="logout"]')
    LOCATOR_BTN_SUBMIT = (By.XPATH, '//button[@id="submit"]')
    LOCATOR_BTN_CANCEL = (By.XPATH, '//button[@id="cancel"]')


class CommonElementsHelper(BasePage):

    def get_page_title(self, page_header):
        return self.find_element_visible((
            CommonElementsLocators.LOCATOR_PAGE_TITLE[0],
            CommonElementsLocators.LOCATOR_PAGE_TITLE[1].format(header=page_header)))

    def get_btn_logout(self):
        return self.find_element_visible(CommonElementsLocators.LOCATOR_BTN_LOGOUT)

    def get_btn_submit(self):
        return self.find_element_visible(CommonElementsLocators.LOCATOR_BTN_SUBMIT)

    def get_btn_cancel(self):
        return self.find_element_visible(CommonElementsLocators.LOCATOR_BTN_CANCEL)
