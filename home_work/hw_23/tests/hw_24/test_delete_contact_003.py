import pytest
from loguru import logger

from home_work.hw_23.pages.add_user_page import AddUserPageHelper
from home_work.hw_23.pages.common_el_page import CommonElementsHelper
from home_work.hw_23.pages.contact_add_page import AddContactHelper
from home_work.hw_23.pages.contact_details_page import ContactDetailsHelper
from home_work.hw_23.pages.contact_list_page import ContactListHelper
from home_work.hw_23.urls.site_page_urls import PageUrls
from home_work.hw_23.utils.constants.site_headers_names import Headers


@pytest.mark.parametrize("browsers_chrome", [1], indirect=True)
def test_delete_contact_003(browsers_chrome):
    browser = browsers_chrome[0]

    logger.info('Create Helpers Instances')
    common_elements_helper = CommonElementsHelper(browser)
    contact_details_helper = ContactDetailsHelper(browser)
    add_user_page_helper = AddUserPageHelper(browser)
    contact_list_helper = ContactListHelper(browser)
    add_contact_helper = AddContactHelper(browser)

    logger.info('Go to adding user page')
    add_user_page_helper.get_url(PageUrls.PAGE_ADD_USER_URL)

    logger.info("Create Main User")
    add_user_page_helper.register_main_user()

    logger.info(f'Check header {Headers.CONTACT_LIST}')
    common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    logger.info('Click on button "Add new contact"')
    contact_list_helper.get_btn_add_new_contact().click()

    logger.info(f'Check header {Headers.ADD_CONTACT}')
    common_elements_helper.get_page_title(Headers.ADD_CONTACT)

    logger.info('Fill all inputs for new contact')
    add_contact_helper.fill_contact_with_random_data()
    common_elements_helper.get_btn_submit().click()

    logger.info(f'Check header {Headers.CONTACT_LIST}')
    common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    logger.info('One client appeared in the table')
    expected_number_of_rows = 1
    actual_number_of_rows = len(contact_list_helper.get_all_table_rows())

    assert expected_number_of_rows == actual_number_of_rows, \
        (f"\nExpected number of rows: {expected_number_of_rows}"
         f"\nActual number of rows: {actual_number_of_rows}")

    logger.info('Click on first row in the table')
    contact_list_helper.get_all_table_rows()[0].click()

    logger.info(f'Check header {Headers.CONTACT_DETAILS}')
    common_elements_helper.get_page_title(Headers.CONTACT_DETAILS)

    logger.info('Click on "Delete Contact" button')
    contact_details_helper.get_btn_delete_contact().click()

    logger.info('Submit contact deleting')
    contact_details_helper.confirmation_alert_confirm()

    logger.info(f'Check header {Headers.CONTACT_LIST}')
    common_elements_helper.get_page_title(Headers.CONTACT_LIST)

    logger.info("Check that no contact in the contact list table")
    contact_list_helper.get_all_table_rows(visible=False)
