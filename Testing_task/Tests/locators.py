from selenium.webdriver.common.by import By

class LoginPageLocators(object):

    GO_BUTTON = (By.ID, 'submit')
    SIGNUP_LNK = (By.PARTIAL_LINK_TEXT, 'Sign up')
    REGISTRATION_HEADER_IN_LOGIN_PAGE = (By.XPATH, './/*[text()[contains(.,"Thank you for signing up for Snovio. Please, check your email to confirm registration.")]]')


class RegistrationPageLocators(object):

    NAME_FLD = (By.NAME, 'name')
    EMAIL_FLD = (By.NAME, 'email')
    PSWRD_FLD = (By.NAME, 'password')
    CONFIRM_PSWRD_FLD = (By.NAME, 'password_confirmation')

    SIGN_UP_BTN = (By.XPATH, './/*[@class="btn btn-primary btn-lg btn-progress"]')
    TERMS_LNK = (By.PARTIAL_LINK_TEXT, 'Terms of Service')
    PPOLICY_LNK = (By.PARTIAL_LINK_TEXT, 'Privacy Policy')
    LOGIN_LNK = (By.PARTIAL_LINK_TEXT, 'Login')

    HAS_ERROR_FLD = (By.XPATH, './/*[@class="form-group has-error"]/label[@class]')

    HAS_ERROR_FLD_TEXT = { 'byname': By.XPATH, 'valuename':'.//*[@class="form-group has-error"]/label[text()="{0}"]/../span/strong'}
    ERROR_REGIASTRATION_HEADER = (By.XPATH, './/*[text() ="Incorrect input data"]')

    ERROR_REGIASTRATION_HEADER_FAKE_EMAIL = (By.XPATH, './/*[text()[contains(.,"Signups from disposable temporary emails are not allowed")]]')


class TmpMailPageLocators(object):

    EMAIL_1_FLD = (By.XPATH, './/input[@id="home-email"]')
    EMAIL_2_FLD = (By.XPATH, './/span[@id="domain"]')


class TempMailPageLocators(object):
    REFRESH_BTN = (By.XPATH,'.//a[@id="resetSessionLifeButton"]')
    EMAIL_FLD = (By.XPATH,'.//input[@id="mailAddress"]')
    TITLE_LETTER = (By.XPATH, './/span[text()="Confirm Snovio Account"]')
    BTN_OPEN_LETTER = (By.XPATH, './/*[@id="ui-id-1"]')


    STR_1_LETTER_TEXT = (By.XPATH,'.//div[@id="ui-id-2"]/div/p[2]')
    STR_2_LETTER_TEXT = (By.XPATH,'.//div[@id="ui-id-2"]/div/p[3]')
    STR_3_LETTER_TEXT = (By.XPATH,'.//div[@id="ui-id-2"]/div//p[4]')
    CONFIRM_LINK = (By.XPATH,'.//div[@id="ui-id-2"]/div//p[5]/a')