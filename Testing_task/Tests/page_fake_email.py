from locators import TmpMailPageLocators
from selenium import webdriver



class Page_TmpMail(object):

    TMP_MAIL_PAGE_TITLE = "Fake Mail Generator - Free temporary email addresses"
    TMP_MAIL_URL = "http://www.fakemailgenerator.com/"

    driver = ""

    def open_fakeEmail_page(object):
        object.driver = webdriver.Chrome()
        driver = object.driver
        driver.get(object.TMP_MAIL_URL)
        driver.implicitly_wait(30) # seconds

    def is_tmp_mail_title_matches(self):
        return  self.TMP_MAIL_PAGE_TITLE  in self.driver.title

    def get_email_part_1(self):
        element = self.driver.find_element(*TmpMailPageLocators.EMAIL_1_FLD).get_attribute('value')
        return element


    def get_email_part_2(self):
        element = self.driver.find_element(*TmpMailPageLocators.EMAIL_2_FLD).text
        return element
