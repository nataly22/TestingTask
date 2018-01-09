# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from registrationPage import RegistrPage
import page_TermsAndService
import page_PrivacyPolicy
from page_Login import Page_Login
from global_methods import Global_Methods
from registrationProfile import RegistrationProfile
from locators import RegistrationPageLocators


class RegistrationTests(unittest.TestCase):


    #def setUp(self):
    #    self.driver = webdriver.Chrome()
    #    self.driver.get("https://app.snov.io/register")
    reg_page = RegistrPage()
    login_page = Page_Login()

    driver = ""


    def test_registration_positive(self):
        """Positive test for check redirect on login page after btn Sign In click"""
        print('========================================================================')
        print('Positive test for check redirect on login page after btn Sign In click')
        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver


        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"
        #fill all registartion fields


        prifileObj = RegistrationProfile()
        email_registration = prifileObj.get_random_email()

        self.reg_page.fill_name(prifileObj.new_user_date['name'])
        self.reg_page.fill_email(email_registration)
        self.reg_page.fill_password(prifileObj.new_user_date['password'])
        self.reg_page.fill_confirm_password(prifileObj.new_user_date['confirm_password'])
        self.reg_page.click_sign_up_btn()


        #print reg_page.get_login_title()
        #assert reg_page.is_login_title_matches(), "Login title page doesn't match"
        time.sleep(1)
        assert self.reg_page.get_login_title() == 'Snov.io Log In',"Login title page doesn't match"
        print('---------  SUCCESS test_registration_positive -----------')
        driver.quit()

    def test_viewTermsOfServicePage(self):
        """Test for check redirect on TermsOfService page after link TermsOfService click"""
        print('========================================================================')
        print('Test for check redirect on TermsOfService page after link TermsOfService click')
        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        self.reg_page.click_terms_lnk()
        terms_page = page_TermsAndService.Page_TermsAndService(driver)


        driver.get(terms_page.TERMS_URL)
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.title_is(terms_page.get_terms_title()))
        assert terms_page.get_terms_title() == 'Snovio terms and conditions', "Terms title page doesn't match"

        print('---------  SUCCESS test_viewTermsOfServicePage-----------')
        driver.quit()

    def test_viewPrivacyPolicyPage(self):
        """Test for check redirect on PrivacyPolicy page after link PrivacyPolicy click"""
        print('========================================================================')
        print('Test for check redirect on PrivacyPolicy page after link PrivacyPolicy click')
        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        self.reg_page.click_privacyPolicy_lnk()
        ppolicy_page = page_PrivacyPolicy.Page_PrivacyPolicy(driver)

        driver.get(ppolicy_page.PPOLICY_URL)
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.title_contains('Privacy Policy'))
        assert ppolicy_page.get_ppolicy_title().find("Privacy Policy") != -1, "Privacy Policy title page doesn't match"

        print('---------  SUCCESS test_viewPrivacyPolicyPage-----------')
        driver.quit()

    def test_directOnLoginPage(self):
        """Test for check redirect on Login page after link Login click"""
        print('========================================================================')
        print('Test for check redirect on Login page after link Login click')
        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        self.reg_page.click_login_lnk()

        #driver.get(self.login_page.LOGIN_URL)
        #wait = WebDriverWait(driver, 20)
        #element = wait.until(EC.title_is(self.reg_page.get_login_title()))

        time.sleep(2)
        assert self.reg_page.is_login_title_matches(), "Login title page doesn't match"
        print('---------  SUCCESS test_directOnLoginPage-----------')
        driver.quit()

    def test_registration_requirementsFields(self):
        """Negative test for check the validation of requirements fields on registration fields"""
        print('========================================================================')
        print('Negative test for check the validation of requirements fields on registration fields')
        # Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        # cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        self.reg_page.click_sign_up_btn()

        #test that regiastartion page is opened
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        time.sleep(1)
        #get count elements with error message
        cnt_error = self.reg_page.get_count_hasError_fields()
        print('cnt_error='+str(cnt_error))

        #check that we have right the error elements count

        assert cnt_error == prifileObj.count_registration_hasError_fields, \
            "Count requirements fields has Errors doesn't match"

        # check that we have right the header about incorrect input dara
        assert self.reg_page.is_error_validation_header(), "No error header"

        #check that each required field has uder the right error validation text

        #check field Name
        assert self.reg_page.get_hasError_validation_text_for_field('Name') == prifileObj.valid_requirement_text_for_name, \
            "No validation message for Name field"
        #check field  Email Adress
        assert self.reg_page.get_hasError_validation_text_for_field('E-Mail Address') == prifileObj.valid_requirement_text_for_email, \
            "No validation message for Email field"
        # check field  Password
        assert self.reg_page.get_hasError_validation_text_for_field(
            'Password') == prifileObj.valid_requirement_text_for_password, \
            "No validation message for Password field"

        print('---------  SUCCESS test_registration_requirementsFields  -----------')
        driver.quit()



    def test_registration_empty_Fields(self):
        """Negative test for check the validation entering the strigs with spaces on registration fields"""
        print('========================================================================')
        print('Negative test for check the validation entering the strigs with spaces on registration fields')
        # Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        # cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        str_with_spaces = '         '

        self.reg_page.fill_name(str_with_spaces)
        self.reg_page.fill_email(str_with_spaces)
        self.reg_page.fill_password(str_with_spaces)
        self.reg_page.fill_confirm_password(str_with_spaces)

        self.reg_page.click_sign_up_btn()

        #test that regiastartion page is opened
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        time.sleep(3)
        #get count elements with error message
        cnt_error = self.reg_page.get_count_hasError_fields()
        print('cnt_error='+str(cnt_error))

        #check that we have right the error elements count

        assert cnt_error == prifileObj.count_registration_hasError_fields, \
            "Count requirements fields has Errors doesn't match"

        # check that we have right the header about incorrect input dara
        assert self.reg_page.is_error_validation_header(), "No error header"

        #check that each required field has uder the right error validation text

        #check field Name
        assert self.reg_page.get_hasError_validation_text_for_field('Name') == prifileObj.valid_requirement_text_for_name, \
            "No validation message for Name field"
        #check field  Email Adress
        assert self.reg_page.get_hasError_validation_text_for_field('E-Mail Address') == prifileObj.valid_requirement_text_for_email, \
            "No validation message for Email field"
        # check field  Password
        assert self.reg_page.get_hasError_validation_text_for_field(
            'Password') == prifileObj.valid_requirement_text_for_password, \
            "No validation message for Password field"

        print('---------  SUCCESS test_registration_empty_Fields  -----------')
        driver.quit()



    def test_registration_entering_an_existing_email(self):
        """Negative test for check validation on entering an existing email"""
        print('========================================================================')
        print('Negative test for check validation on entering an existing email')
        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"
        #fill all registartion fields

        prifileObj = RegistrationProfile()
        email_registration = prifileObj.get_random_email()

        #First registration with some email
        self.reg_page.fill_name(prifileObj.new_user_date['name'])
        self.reg_page.fill_email(email_registration)
        self.reg_page.fill_password(prifileObj.new_user_date['password'])
        self.reg_page.fill_confirm_password(prifileObj.new_user_date['confirm_password'])
        self.reg_page.click_sign_up_btn()


        time.sleep(2)
        assert self.reg_page.is_login_title_matches(), "Login title page doesn't match"

        driver.quit()

        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver


        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        # Second registration with the same  email
        self.reg_page.fill_name(prifileObj.new_user_date['name'])
        self.reg_page.fill_email(email_registration)
        self.reg_page.fill_password(prifileObj.new_user_date['password'])
        self.reg_page.fill_confirm_password(prifileObj.new_user_date['confirm_password'])
        self.reg_page.click_sign_up_btn()
        time.sleep(2)
        # test that regiastartion page is opened
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()
        #check that we have right the error elements count


        # get count elements with error message
        cnt_error = self.reg_page.get_count_hasError_fields()
        print('cnt='+str(cnt_error))
        assert cnt_error == prifileObj.count_registration_hasError_fields_entering_existing_email, \
            "Count fields has Errors doesn't match"

        # check that we have right the header about incorrect input dara
        assert self.reg_page.is_error_validation_header(), "No error header"

        #check that each required field has uder the right error validation text

        #check field  Email Adress
        assert self.reg_page.get_hasError_validation_text_for_field('E-Mail Address') == prifileObj.valid_exist_for_email_text, \
            "No validation message for Email field"

        print('---------  SUCCESS test_registration_entering_an_existing_email -----------')
        driver.quit()


    def test_validation_name_field(self):
        """Test for check validation Name field"""
        print('========================================================================')
        print('Test for check validation Name field')
        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"



        prifileObj = RegistrationProfile()
        #=========================================================================
        #check field name when field name is right (has 255 lendth)
        self.reg_page.fill_name(prifileObj.name_255_length)

        self.reg_page.click_sign_up_btn()

        #check has field Name error text
        global_m = Global_Methods(driver)
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Name') == False, \
            "The Name field is right. There should be no message about error for Name field long"

        # =========================================================================
        # check field name when field name has more than 255 long and isn' right (has 256 lendth)
        self.reg_page.clear_name()
        #time.sleep(3)
        self.reg_page.fill_name(prifileObj.name_256_length)

        self.reg_page.click_sign_up_btn()
        time.sleep(1)
        # check has field Name error text and this validation text is right
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Name') == True, \
            "The Name field is not right. There should be message about error for Name field long"

        # check field Name on right error message about length
        assert self.reg_page.get_hasError_validation_text_for_field('Name') == prifileObj.valid_for_long_name_text, \
            "No validation message for Name field about it's long"

        # =========================================================================
        # check field name when field name has different characters not lattes and not numbers
        self.reg_page.clear_name()
        self.reg_page.fill_name(prifileObj.name_with_different_characters)

        self.reg_page.click_sign_up_btn()
        time.sleep(1)
        # check has field Name error text and this validation text is right
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Name') == False, \
            "The Name field is right. There should be no message about error for Name field"

        # =========================================================================
        # check field name when field name has capital letters
        self.reg_page.clear_name()
        self.reg_page.fill_name(prifileObj.name_with_capital_letters)

        self.reg_page.click_sign_up_btn()
        time.sleep(1)
        # check has field Name error text and this validation text is right
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Name') == False, \
            "The Name field is right. There should be no message about error for Name field"


        # =========================================================================
        # check field name when field name has cirillic letters
        self.reg_page.clear_name()
        self.reg_page.fill_name(prifileObj.name_with_cirillic_letters)

        self.reg_page.click_sign_up_btn()
        time.sleep(1)
        # check has field Name error text and this validation text is right
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Name') == False, \
            "The Name field is right. There should be no message about error for Name field"

        # =========================================================================
        # check field name when field name has one letter
        self.reg_page.clear_name()
        self.reg_page.fill_name(prifileObj.name_with_one_letter)

        self.reg_page.click_sign_up_btn()
        time.sleep(1)
        # check has field Name error text and this validation text is right
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Name') == False, \
            "The Name field is right. There should be no message about error for Name field"

        print('---------  SUCCESS test_validation_name_field -----------')
        driver.quit()

    def tear_down(self):
        self.reg_page.driver.quit()


if __name__ == "__main__":
    unittest.main()