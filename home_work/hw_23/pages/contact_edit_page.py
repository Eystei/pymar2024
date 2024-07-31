from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from home_work.hw_23.pages._base_page import BasePage
from home_work.hw_23.utils.rand_methods import Randoms


class ContactEditPage:
    LOCATOR_INPUT_FIRST_NAME = (By.XPATH, '//input[@id="firstName"]')
    LOCATOR_INPUT_LAST_NAME = (By.XPATH, '//input[@id="lastName"]')
    LOCATOR_INPUT_DATE_OF_BIRTH = (By.XPATH, '//input[@id="birthdate"]')
    LOCATOR_INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
    LOCATOR_INPUT_PHONE = (By.XPATH, '//input[@id="phone"]')
    LOCATOR_INPUT_STR_ADDRESS_ONE = (By.XPATH, '//input[@id="street1"]')
    LOCATOR_INPUT_STR_ADDRESS_TWO = (By.XPATH, '//input[@id="street2"]')
    LOCATOR_INPUT_CITY = (By.XPATH, '//input[@id="city"]')
    LOCATOR_INPUT_STATE_OF_PROVINCE = (By.XPATH, '//input[@id="stateProvince"]')
    LOCATOR_INPUT_POSTAL_CODE = (By.XPATH, '//input[@id="postalCode"]')
    LOCATOR_INPUT_COUNTRY = (By.XPATH, '//input[@id="country"]')


class ContactEditHelper(BasePage):

    def get_input_first_name(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_FIRST_NAME)

    def get_input_last_name(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_LAST_NAME)

    def get_input_date_of_birth(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_DATE_OF_BIRTH)

    def get_input_email(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_EMAIL)

    def get_input_phone(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_PHONE)

    def get_input_str_address_one(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_STR_ADDRESS_ONE)

    def get_input_str_address_two(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_STR_ADDRESS_TWO)

    def get_input_city(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_CITY)

    def get_input_state_of_province(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_STATE_OF_PROVINCE)

    def get_input_postal_code(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_POSTAL_CODE)

    def get_input_country(self):
        return self.find_element_visible(ContactEditPage.LOCATOR_INPUT_COUNTRY)

    """ METHODS """

    def refill_contact_inputs_with_random_data(
            self,
            *,
            first_name: bool = False,
            last_name: bool = False,
            date_of_birth: bool = False,
            email: bool = False,
            phone: bool = False,
            str_address_one: bool = False,
            str_address_two: bool = False,
            city: bool = False,
            state_of_province: bool = False,
            postal_code: bool = False,
            country: bool = False,
            all_fields: bool = False
    ):
        if all_fields or first_name:
            self.get_input_first_name().send_keys(Keys.CONTROL + "A")
            self.get_input_first_name().send_keys(Randoms.rand_word(length=10))

        if all_fields or last_name:
            self.get_input_last_name().send_keys(Keys.CONTROL + "A")
            self.get_input_last_name().send_keys(Randoms.rand_word(length=10))

        if all_fields or date_of_birth:
            self.get_input_date_of_birth().send_keys(Keys.CONTROL + "A")
            self.get_input_date_of_birth().send_keys(Randoms.date_of_birth())

        if all_fields or email:
            self.get_input_email().send_keys(Keys.CONTROL + "A")
            self.get_input_email().send_keys(Randoms.email_gen(length=10))

        if all_fields or phone:
            self.get_input_phone().send_keys(Keys.CONTROL + "A")
            self.get_input_phone().send_keys(Randoms.int_gen(length=10))

        if all_fields or str_address_one:
            self.get_input_str_address_one().send_keys(Keys.CONTROL + "A")
            self.get_input_str_address_one().send_keys(Randoms.rand_word(length=15))

        if all_fields or str_address_two:
            self.get_input_str_address_two().send_keys(Keys.CONTROL + "A")
            self.get_input_str_address_two().send_keys(Randoms.rand_word(length=15))

        if all_fields or city:
            self.get_input_city().send_keys(Keys.CONTROL + "A")
            self.get_input_city().send_keys(Randoms.rand_word(length=10))

        if all_fields or state_of_province:
            self.get_input_state_of_province().send_keys(Keys.CONTROL + "A")
            self.get_input_state_of_province().send_keys(Randoms.rand_word(length=10))

        if all_fields or postal_code:
            self.get_input_postal_code().send_keys(Keys.CONTROL + "A")
            self.get_input_postal_code().send_keys(Randoms.int_gen(length=4))

        if all_fields or country:
            self.get_input_country().send_keys(Keys.CONTROL + "A")
            self.get_input_country().send_keys(Randoms.rand_word(length=10))
