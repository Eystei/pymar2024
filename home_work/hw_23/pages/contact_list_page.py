from selenium.webdriver.common.by import By

from home_work.hw_23.pages._base_page import BasePage


class ContactListLocators:
    LOCATOR_BTN_ADD_NEW_CONTACT = (By.XPATH, '//button[@id="add-contact"]')

    LOCATOR_ALL_TABLE_CELLS = (By.XPATH, '//table/tr')
    LOCATOR_TABLE_CELL_NAME = (By.XPATH, '//tr[td[text()="{contact_id}"]]/td[2]')
    LOCATOR_TABLE_CELL_BIRTHDATE = (By.XPATH, '//tr[td[text()="{contact_id}"]]/td[3]')
    LOCATOR_TABLE_CELL_EMAIL = (By.XPATH, '//tr[td[text()="{contact_id}"]]/td[4]')
    LOCATOR_TABLE_CELL_PHONE = (By.XPATH, '//tr[td[text()="{contact_id}"]]/td[5]')
    LOCATOR_TABLE_CELL_ADDRESS = (By.XPATH, '//tr[td[text()="{contact_id}"]]/td[6]')
    LOCATOR_TABLE_CELL_CITY_STATE_POSTAL = (By.XPATH, '//tr[td[text()="{contact_id}"]]/td[7]')
    LOCATOR_TABLE_CELL_COUNTRY = (By.XPATH, '//tr[td[text()="{contact_id}"]]/td[8]')


class ContactListHelper(BasePage):

    def get_btn_add_new_contact(self):
        return self.find_element_visible(ContactListLocators.LOCATOR_BTN_ADD_NEW_CONTACT)

    def get_all_table_rows(self, visible=True):
        if visible:
            return self.find_all_elements(ContactListLocators.LOCATOR_ALL_TABLE_CELLS)
        return self.element_invisible(ContactListLocators.LOCATOR_ALL_TABLE_CELLS)

    def get_table_cell_name(self, contact_id):
        return self.find_element_visible(
            ContactListLocators.LOCATOR_TABLE_CELL_NAME[0],
            ContactListLocators.LOCATOR_TABLE_CELL_NAME[1].format(contact_id=contact_id)
        )

    def get_table_cell_birthdate(self, contact_id):
        return self.find_element_visible(
            ContactListLocators.LOCATOR_TABLE_CELL_BIRTHDATE[0],
            ContactListLocators.LOCATOR_TABLE_CELL_BIRTHDATE[1].format(contact_id=contact_id)
        )

    def get_table_cell_email(self, contact_id):
        return self.find_element_visible(
            ContactListLocators.LOCATOR_TABLE_CELL_EMAIL[0],
            ContactListLocators.LOCATOR_TABLE_CELL_EMAIL[1].format(contact_id=contact_id)
        )

    def get_table_cell_phone(self, contact_id):
        return self.find_element_visible(
            ContactListLocators.LOCATOR_TABLE_CELL_PHONE[0],
            ContactListLocators.LOCATOR_TABLE_CELL_PHONE[1].format(contact_id=contact_id)
        )

    def get_table_cell_address(self, contact_id):
        return self.find_element_visible(
            ContactListLocators.LOCATOR_TABLE_CELL_ADDRESS[0],
            ContactListLocators.LOCATOR_TABLE_CELL_ADDRESS[1].format(contact_id=contact_id)
        )

    def get_table_cell_city_state_postal(self, contact_id):
        return self.find_element_visible(
            ContactListLocators.LOCATOR_TABLE_CELL_CITY_STATE_POSTAL[0],
            ContactListLocators.LOCATOR_TABLE_CELL_CITY_STATE_POSTAL[1].format(contact_id=contact_id)
        )

    def get_table_cell_country(self, contact_id):
        return self.find_element_visible(
            ContactListLocators.LOCATOR_TABLE_CELL_COUNTRY[0],
            ContactListLocators.LOCATOR_TABLE_CELL_COUNTRY[1].format(contact_id=contact_id)
        )
