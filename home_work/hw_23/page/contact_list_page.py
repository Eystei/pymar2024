class ContactListLocators:
    LOCATOR_BTN_ADD_NEW_CONTACT = '//button[@id="add-contact"]'

    LOCATOR_TABLE_CELL_NAME = '//tr[td[text()="{contact_id}"]]/td[2]'
    LOCATOR_TABLE_CELL_BIRTHDATE = '//tr[td[text()="{contact_id}"]]/td[3]'
    LOCATOR_TABLE_CELL_EMAIL = '//tr[td[text()="{contact_id}"]]/td[4]'
    LOCATOR_TABLE_CELL_PHONE = '//tr[td[text()="{contact_id}"]]/td[5]'
    LOCATOR_TABLE_CELL_ADDRESS = '//tr[td[text()="{contact_id}"]]/td[6]'
    LOCATOR_TABLE_CELL_CITY_STATE_POSTAL = '//tr[td[text()="{contact_id}"]]/td[7]'
    LOCATOR_TABLE_CELL_COUNTRY = '//tr[td[text()="{contact_id}"]]/td[8]'
