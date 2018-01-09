# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import time
from registrationPage import RegistrPage
from global_methods import Global_Methods
from registrationProfile import RegistrationProfile
from locators import RegistrationPageLocators


class ValidationEmailRegistrationTests(unittest.TestCase):
    reg_page = RegistrPage()
    driver = ""

    def test_validation_email_with_capital_letters(self):
        """Test for check validation Email field"""
        print('========================================================================')
        print('Test for check validation Email field with capital letters')

        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        #check field email when field email  contains the capital letters
        self.reg_page.fill_email(prifileObj.email_with_capital_letters)

        self.reg_page.click_sign_up_btn()

        # check has field Email error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'E-Mail Address') == False, \
            "The Email field is right. There should be no message about error for Email field for email with capital letters"
        print('---------  SUCCESS test_validation_email_with_capital_letters -----------')
        driver.quit()

    def test_validation_email_without_point_after_dog(self):
        """Test for check validation Email field  when email without point after dog"""
        print('========================================================================')
        print('Test for check validation Email field  when email without point after dog')

        # Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)
        # cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()
        self.reg_page.fill_email(prifileObj.email_without_point)

        self.reg_page.click_sign_up_btn()

        #time.sleep(2)

        # check has field Email error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'E-Mail Address') == True, \
            "The Email field is not right. There should be message about error for Email field for email without point after dog"

        # check field Email on right error message about not valid field
        assert self.reg_page.get_hasError_validation_text_for_field('E-Mail Address') == prifileObj.no_valid_for_email_text, \
            "No validation message for Email field about it'is not valid"


        print('---------  SUCCESS test_validation_email_without_point_after_dog -----------')
        driver.quit()


    def test_validation_email_with_numbers_after_dog(self):
        """Test for check validation Email field  when email with numbers after dog"""
        print('========================================================================')
        print('Test for check validation Email field  when email with numbers after dog')

        # Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)
        # cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        self.reg_page.fill_email(prifileObj.email_with_numbers_after_dog)

        self.reg_page.click_sign_up_btn()

        #time.sleep(2)

        # check has field Email error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'],
                                          'E-Mail Address') == False, \
            "The Email field is  right. There should be no message about error for Email field for email with numbers after dog"
        print('---------  SUCCESS test_validation_email_with_numbers_after_dog -----------')
        driver.quit()

    def test_validation_email_with_other_characters_befor_dog(self):
        """Test for check field email when email contains other characters befor dog"""
        print('========================================================================')
        print('Test for check field email when email contains other characters befor dog')

        # Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        # cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        self.reg_page.fill_email(prifileObj.email_with_other_characters_befor_dog)

        self.reg_page.click_sign_up_btn()

        #time.sleep(2)

        # check has field Email error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'],
                                          'E-Mail Address') == False, \
            "The Email field is  right. There should be no message about error for email with \
with other characters befor dog"
        print('---------  SUCCESS test_validation_email_with_other_characters_befor_dog -----------')
        driver.quit()


    def test_validation_email_with_max_length_64_befor_dog(self):
        """Test for check field email when email with email with max length 64 befor dog"""
        print('========================================================================')
        print('est for check field email when email with email with max length 64 befor dog')

        # Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        # cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        self.reg_page.fill_email(prifileObj.email_with_max_length_64_befor_dog)

        self.reg_page.click_sign_up_btn()

        #time.sleep(2)

        # check has field Email error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'],
                                          'E-Mail Address') == False, \
            "The Email field is  right. There should be no message about error for  email with  \
with max length 64 befor dog"
        print('---------  SUCCESS test_validation_email_with_max_length_64_befor_dog -----------')
        driver.quit()


    def test_validation_email_with_max_length_greater_64_befor_dog(self):
        """Test for check field email when email with email with max length greater 64 befor dog"""
        print('========================================================================')
        print('Test for check field email when email with email with max length greater 64 befor dog')

        # Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        # cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        self.reg_page.fill_email(prifileObj.email_with_max_length_greater_64_befor_dog)

        self.reg_page.click_sign_up_btn()

        #time.sleep(2)

        # check has field Email error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'],
                                          'E-Mail Address') == True, \
            "The Email field is not right. There should be message about error for Email field for email \
with email_with_max_length_greater_64_befor_dog"

        # check field Email on right error message about not valid field
        assert self.reg_page.get_hasError_validation_text_for_field('E-Mail Address') == prifileObj.no_valid_for_email_text, \
            "No validation message for Email field about it'is not valid"

        print('---------  SUCCESS test_validation_email_with_max_length_64_befor_dog -----------')
        driver.quit()

    def test_validation_email_with_point_befor_dog(self):
        """Test for check field email when email with point befor dog"""
        print('========================================================================')
        print('Test for check field email when email with point befor dog')

        # Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        # cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        self.reg_page.fill_email(prifileObj.email_with_point_befor_dog)

        self.reg_page.click_sign_up_btn()

        #time.sleep(2)

        # check has field Email error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'],
                                          'E-Mail Address') == False, \
            "The Email field is right. There should be no message about error for Email with point befor dog"

        print('---------  SUCCESS test_validation_email_with_point_befor_dog -----------')
        driver.quit()

    def test_validation_email_without_dog(self):
        """Test for check field email when email without dog"""
        print('========================================================================')
        print('Test for check field email when email without dog')

        # Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        # cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        self.reg_page.fill_email(prifileObj.email_without_dog)

        self.reg_page.click_sign_up_btn()

        #time.sleep(2)

        # check has field Email error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'],
                                          'E-Mail Address') == False, "The Email field is right. \
There should be no message about error for Email with point befor dog"
        print('---------  SUCCESS test_validation_email_without_dog -----------')
        driver.quit()


    def tear_down(self):
        self.reg_page.driver.quit()


if __name__ == "__main__":
    unittest.main()