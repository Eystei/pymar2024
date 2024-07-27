from home_work.hw_23.page.add_user_page import AddUserPageLocators
from home_work.hw_23.page.common_el_page import CommonElementsLocators
from home_work.hw_23.page.contact_add_page import AddContactLocators
from home_work.hw_23.page.contact_details_page import ContactDetailsPage
from home_work.hw_23.page.contact_edit_page import ContactEditPage
from home_work.hw_23.page.contact_list_page import ContactListLocators
from home_work.hw_23.page.login_page import LoginPageLocators


def print_(str_):
    print(f"\033[1;94m{str_}\033[0m")


def test_contact_crud_hw_23():
    TEST_CONTACT_ID = '0000000000'

    print_('\nLogin Page')
    print(f'Click Signup Button: {LoginPageLocators.LOCATOR_BTN_SIGN_UP}')

    print_('\nAdd New User')
    print(f'Fill First Name Input: {AddUserPageLocators.LOCATOR_INPUT_FIRST_NAME}')
    print(f'Fill Last Name Input: {AddUserPageLocators.LOCATOR_INPUT_LAST_NAME}')
    print(f'Fill Email Input: {AddUserPageLocators.LOCATOR_INPUT_EMAIL}')
    print(f'Fill Password Input: {AddUserPageLocators.LOCATOR_INPUT_PASSWORD}')
    print(f"Click Submit: {CommonElementsLocators.LOCATOR_BTN_SUBMIT}")

    print_('\nAdd First New Contact')
    print(f"Click Add New Contact: {ContactListLocators.LOCATOR_BTN_ADD_NEW_CONTACT}")

    print(f"Fill First Name Input: {AddContactLocators.LOCATOR_INPUT_FIRST_NAME}")
    print(f"Fill Last Name Input: {AddContactLocators.LOCATOR_INPUT_LAST_NAME}")
    print(f"Fill Birth Name Input: {AddContactLocators.LOCATOR_INPUT_DATE_OF_BIRTH}")
    print(f"Fill Email Name Input: {AddContactLocators.LOCATOR_INPUT_EMAIL}")
    print(f"Fill Phone Name Input: {AddContactLocators.LOCATOR_INPUT_PHONE}")
    print(f"Fill Address1 Name Input: {AddContactLocators.LOCATOR_INPUT_STR_ADDRESS_ONE}")
    print(f"Fill Address2 Name Input: {AddContactLocators.LOCATOR_INPUT_STR_ADDRESS_TWO}")
    print(f"Fill City Name Input: {AddContactLocators.LOCATOR_INPUT_CITY}")
    print(f"Fill State Name Input: {AddContactLocators.LOCATOR_INPUT_STATE_OF_PROVINCE}")
    print(f"Fill Postal Name Input: {AddContactLocators.LOCATOR_INPUT_POSTAL_CODE}")
    print(f"Fill Country Name Input: {AddContactLocators.LOCATOR_INPUT_COUNTRY}")

    print(f"Click Submit: {CommonElementsLocators.LOCATOR_BTN_SUBMIT}")

    print_('\nAdd Second New Contact')
    print(f"Click Add New Contact: {ContactListLocators.LOCATOR_BTN_ADD_NEW_CONTACT}")

    print(f"Fill First Name Input: {AddContactLocators.LOCATOR_INPUT_FIRST_NAME}")
    print(f"Fill Last Name Input: {AddContactLocators.LOCATOR_INPUT_LAST_NAME}")
    print(f"Fill Birth Name Input: {AddContactLocators.LOCATOR_INPUT_DATE_OF_BIRTH}")
    print(f"Fill Email Name Input: {AddContactLocators.LOCATOR_INPUT_EMAIL}")
    print(f"Fill Phone Name Input: {AddContactLocators.LOCATOR_INPUT_PHONE}")
    print(f"Fill Address1 Name Input: {AddContactLocators.LOCATOR_INPUT_STR_ADDRESS_ONE}")
    print(f"Fill Address2 Name Input: {AddContactLocators.LOCATOR_INPUT_STR_ADDRESS_TWO}")
    print(f"Fill City Name Input: {AddContactLocators.LOCATOR_INPUT_CITY}")
    print(f"Fill State Name Input: {AddContactLocators.LOCATOR_INPUT_STATE_OF_PROVINCE}")
    print(f"Fill Postal Name Input: {AddContactLocators.LOCATOR_INPUT_POSTAL_CODE}")
    print(f"Fill Country Name Input: {AddContactLocators.LOCATOR_INPUT_COUNTRY}")

    print(f"Click Submit: {CommonElementsLocators.LOCATOR_BTN_SUBMIT}")

    print_('\nUpdate Contact')
    print(f"Click on First Contact: {ContactListLocators.LOCATOR_TABLE_CELL_NAME.format(contact_id = TEST_CONTACT_ID)}")
    print(f"Click on Edit Contact: {ContactDetailsPage.LOCATOR_BTN_EDIT_CONTACT}")

    print(f"Update First Name Input: {ContactEditPage.LOCATOR_INPUT_FIRST_NAME}")
    print(f"Update Last Name Input: {ContactEditPage.LOCATOR_INPUT_LAST_NAME}")
    print(f"Update Birth Name Input: {ContactEditPage.LOCATOR_INPUT_DATE_OF_BIRTH}")
    print(f"Update Email Name Input: {ContactEditPage.LOCATOR_INPUT_EMAIL}")
    print(f"Update Phone Name Input: {ContactEditPage.LOCATOR_INPUT_PHONE}")
    print(f"Update Address1 Name Input: {ContactEditPage.LOCATOR_INPUT_STR_ADDRESS_ONE}")
    print(f"Update Address2 Name Input: {ContactEditPage.LOCATOR_INPUT_STR_ADDRESS_TWO}")
    print(f"Update City Name Input: {ContactEditPage.LOCATOR_INPUT_CITY}")
    print(f"Update State Name Input: {ContactEditPage.LOCATOR_INPUT_STATE_OF_PROVINCE}")
    print(f"Update Postal Name Input: {ContactEditPage.LOCATOR_INPUT_POSTAL_CODE}")
    print(f"Update Country Name Input: {ContactEditPage.LOCATOR_INPUT_COUNTRY}")

    print(f"Click Submit: {CommonElementsLocators.LOCATOR_BTN_SUBMIT}")

    print_('\nDelete Contact')
    print(f"Click on First Contact: {ContactListLocators.LOCATOR_TABLE_CELL_NAME.format(contact_id = TEST_CONTACT_ID)}")
    print(f"Click Delete: {ContactDetailsPage.LOCATOR_BTN_DELETE_CONTACT}")

    print_('\nLogout')
    print(f"Click on Logout: {CommonElementsLocators.LOCATOR_BTN_LOGOUT}")
