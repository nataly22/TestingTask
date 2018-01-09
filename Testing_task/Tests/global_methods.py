from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class Global_Methods(BasePage):


    def is_exist_by_xpath(self, xpath, parameter):
        try:
            self.driver.find_element_by_xpath(xpath.format(parameter))
        except NoSuchElementException:
            return False
        return True


