from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOCATOR_INPUT_EMAIL = (By.XPATH, '//input[@id="email"]')
    LOCATOR_INPUT_PASS = (By.XPATH, '//input[@id="password"]')

    LOCATOR_BTN_SIGN_UP = (By.XPATH, '//button[@id="signup"]')
