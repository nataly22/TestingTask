
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class Page_TermsAndService(BasePage):

    TERMS_PAGE_TITLE = "Snovio terms and conditions"
    TERMS_URL = "https://snov.io/t_and_c.html"


    def is_terms_title_matches(self):
        return  self.TERMS_PAGE_TITLE  in self.driver.title

    def get_terms_title(self):
        return self.driver.title


