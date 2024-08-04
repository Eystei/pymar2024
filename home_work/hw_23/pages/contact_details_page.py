from selenium.webdriver.common.by import By

from home_work.hw_23.pages._base_page import BasePage


class ContactDetailsPage:
    LOCATOR_BTN_EDIT_CONTACT = (By.XPATH, '//button[@id="edit-contact"]')
    LOCATOR_BTN_DELETE_CONTACT = (By.XPATH, '//button[@id="delete"]')
    LOCATOR_BTN_RETURN_TO_CONTACT_LIST = (By.XPATH, '//button[@id="return"]')

    LOCATOR_ROW_FIRST_NAME = (By.XPATH, '//span[@id="firstName"]')
    LOCATOR_ROW_LAST_NAME = (By.XPATH, '//span[@id="lastName"]')
    LOCATOR_ROW_DATE_OF_BIRTH = (By.XPATH, '//span[@id="birthdate"]')
    LOCATOR_ROW_EMAIL = (By.XPATH, '//span[@id="email"]')
    LOCATOR_ROW_PHONE = (By.XPATH, '//span[@id="phone"]')
    LOCATOR_ROW_STR_ADDRESS_ONE = (By.XPATH, '//span[@id="street1"]')
    LOCATOR_ROW_STR_ADDRESS_TWO = (By.XPATH, '//span[@id="street2"]')
    LOCATOR_ROW_CITY = (By.XPATH, '//span[@id="city"]')
    LOCATOR_ROW_STATE_OF_PROVINCE = (By.XPATH, '//span[@id="stateProvince"]')
    LOCATOR_ROW_POSTAL_CODE = (By.XPATH, '//span[@id="postalCode"]')
    LOCATOR_ROW_COUNTRY = (By.XPATH, '//span[@id="country"]')


class ContactDetailsHelper(BasePage):

    def get_btn_edit_contact(self):
        return self.find_element_visible(ContactDetailsPage.LOCATOR_BTN_EDIT_CONTACT)

    def get_btn_delete_contact(self):
        return self.find_element_visible(ContactDetailsPage.LOCATOR_BTN_DELETE_CONTACT)
