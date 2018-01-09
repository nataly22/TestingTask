#from element import BasePageElement
from selenium import webdriver
from locators import RegistrationPageLocators

#class BasePage(object):
#    def __init__(self, driver):
#        self.driver = driver

class RegistrPage(object):

    REG_PAGE_TITLE = "Snov.io Sign Up"
    LOGIN_PAGE_TITLE = "Snov.io Log In"

    REG_PAGE_URL = "https://app.snov.io/register"

    driver = ""

    def open_registration_page(object):
        #executable_path=CHROME_WEBDRIVER_PATH
        object.driver = webdriver.Chrome()
        driver = object.driver
        driver.get(object.REG_PAGE_URL)
        driver.implicitly_wait(30) # seconds

    def is_title_matches(self):
        return  self.REG_PAGE_TITLE  in self.driver.title

    def is_login_title_matches(self):
        return  self.LOGIN_PAGE_TITLE  in self.driver.title

    def get_login_title(self):
        return self.driver.title

    def fill_name(self, text):
        element = self.driver.find_element(*RegistrationPageLocators.NAME_FLD)
        element.send_keys(text)

    def get_name(self):
        element = self.driver.find_element(*RegistrationPageLocators.NAME_FLD).text
        return element

    def clear_name(self):
        element = self.driver.find_element(*RegistrationPageLocators.NAME_FLD).clear()

    def clear_email(self):
        element = self.driver.find_element(*RegistrationPageLocators.EMAIL_FLD).clear()


    def fill_email(self, text):
        element = self.driver.find_element(*RegistrationPageLocators.EMAIL_FLD)
        element.send_keys(text)

    def fill_password(self, text):
        element = self.driver.find_element(*RegistrationPageLocators.PSWRD_FLD)
        element.send_keys(text)

    def fill_confirm_password(self, text):
        element = self.driver.find_element(*RegistrationPageLocators.CONFIRM_PSWRD_FLD)
        element.send_keys(text)

    def click_sign_up_btn(self):
        element = self.driver.find_element(*RegistrationPageLocators.SIGN_UP_BTN)
        element.click()

    def click_terms_lnk(self):
        element = self.driver.find_element(*RegistrationPageLocators.TERMS_LNK)
        element.click()

    def click_privacyPolicy_lnk(self):
        element = self.driver.find_element(*RegistrationPageLocators.PPOLICY_LNK)
        element.click()

    def click_login_lnk(self):
        element = self.driver.find_element(*RegistrationPageLocators.LOGIN_LNK)
        element.click()


    def get_count_hasError_fields(self):
        a = []
        a = self.driver.find_elements(*RegistrationPageLocators.HAS_ERROR_FLD)
        elements_cnt = len(a)
        return elements_cnt

    def get_hasError_validation_text_for_field(self, name_field):
        by = RegistrationPageLocators.HAS_ERROR_FLD_TEXT['byname']
        value = RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename']
        element_text = self.driver.find_element(by, value.format(name_field)).text
        return element_text

    def is_error_validation_header(self):
        return self.driver.find_elements(*RegistrationPageLocators.ERROR_REGIASTRATION_HEADER)

    def is_error_validation_header_fake_email(self):
        return self.driver.find_elements(*RegistrationPageLocators.ERROR_REGIASTRATION_HEADER_FAKE_EMAIL)


