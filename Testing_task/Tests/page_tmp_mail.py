from selenium import webdriver

from locators import TempMailPageLocators
from selenium.webdriver.common.by import By



class Page_TempMail(object):

    TEMP_MAIL_PAGE_TITLE = "10 Minute Mail - Temporary E-Mail"
    TEMP_URL = "https://10minutemail.com"

    driver = ""

    def open_tempEmail_page(object):
        object.driver = webdriver.Chrome()
        driver = object.driver
        driver.get(object.TEMP_URL)
        driver.implicitly_wait(30) # seconds

    def open_currentUrl_tempEmail_page(object, url):
        object.driver = webdriver.Chrome()
        driver = object.driver
        driver.get(url)


    def is_tmp_mail_title_matches(self):
        return  self.TEMP_MAIL_PAGE_TITLE  in self.driver.title

    def get_email(self):
        element = self.driver.find_element(*TempMailPageLocators.EMAIL_FLD).get_attribute("value")
        return element

    def open_confirm_letter(self):
        element = self.driver.find_element(*TempMailPageLocators.BTN_OPEN_LETTER)
        element.click()

    def get_letter_text(self):
        letter_text = []
        text1 = self.driver.find_element(*TempMailPageLocators.STR_1_LETTER_TEXT).text
        assert isinstance(text1, object)
        letter_text.append(text1)
        #letter_text.append(self.driver.find_element(*TempMailPageLocators.STR_2_LETTER_TEXT)).text
        #letter_text.append(self.driver.find_element(*TempMailPageLocators.STR_3_LETTER_TEXT)).text
        return letter_text

    def click_confirm_link(self):
        element = self.driver.find_element(*TempMailPageLocators.CONFIRM_LINK)
        element.click()

    def click_refresh(self):
        element = self.driver.find_element(*TempMailPageLocators.REFRESH_BTN)
        element.click()
