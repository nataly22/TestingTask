from locators import LoginPageLocators
from selenium import webdriver



class Page_Login(object):

    LOGIN_PAGE_TITLE = "Snov.io Log In"
    LOGIN_URL = "https://app.snov.io/login"



    driver = ""

    def open_login_page(object):
        object.driver = webdriver.Chrome()
        driver = object.driver
        driver.get(object.LOGIN_URL)
        driver.implicitly_wait(30) # seconds


    def is_login_title_matches(self):
        return  self.LOGIN_PAGE_TITLE  in self.driver.title

    def is_registration_header_matches(self):
        return  self.LOGIN_PAGE_TITLE  in self.driver.title


    def get_login_title(self):
        return self.driver.title

    def click_signup_lnk(self):
        element = self.driver.find_element(*LoginPageLocators.SIGNUP_LNK)
        element.click()

    def is_registration_header(self):
        return self.driver.find_elements(*LoginPageLocators.REGISTRATION_HEADER_IN_LOGIN_PAGE)



