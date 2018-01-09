class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class Page_PrivacyPolicy(BasePage):

    PPOLICY_PAGE_TITLE = "Snovio's Privacy Policy"
    PPOLICY_URL = "https://snov.io/privacy-policy.html"


    def is_ppolicy_title_matches(self):
        return  self.PPOLICY_PAGE_TITLE  in self.driver.title

    def get_ppolicy_title(self):
        return self.driver.title

