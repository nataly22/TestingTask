# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import time
from selenium import webdriver
from registrationPage import RegistrPage
from global_methods import Global_Methods
from registrationProfile import RegistrationProfile
from locators import RegistrationPageLocators


class ValidationEmailRegistrationTests(unittest.TestCase):
    reg_page = RegistrPage()
    driver = ""

    def test_validation_empty_confirm_passwrd(self):
        """Test for check validation requirement field COnfirm password"""
        print('========================================================================')
        print('Test for check validation requirement field COnfirm password')

        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        email_registration = prifileObj.get_random_email()

        self.reg_page.fill_name(prifileObj.new_user_date['name'])
        self.reg_page.fill_email(email_registration)
        self.reg_page.fill_password(prifileObj.new_user_date['password'])

        self.reg_page.click_sign_up_btn()

        time.sleep(2)

        # check has field Password error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Password') == True, \
            "The Confirm password field is not right. There should be message about error for do not match password"

        # check field Password on right error message about not match the password
        assert self.reg_page.get_hasError_validation_text_for_field('Password') == prifileObj.valid_for_not_match_password_text, \
            "No validation message for Password and Confirm password fields are do not matched"


        print('---------  SUCCESS test_validation_empty_confirm_passwrd -----------')
        driver.quit()


    def test_validation_not_match_passwrd_to_confirm_passwrd(self):
        """Test for check validation not matched fields Confirm password and password"""
        print('========================================================================')
        print('Test for check validation not matched fields Confirm password and password')

        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        email_registration = prifileObj.get_random_email()

        self.reg_page.fill_name(prifileObj.new_user_date['name'])
        self.reg_page.fill_email(email_registration)
        self.reg_page.fill_password(prifileObj.new_user_date['password'])
        self.reg_page.fill_confirm_password(prifileObj.new_user_date['not_right_confirm_password'])

        self.reg_page.click_sign_up_btn()

        time.sleep(2)

        # check has field Password error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Password') == True, \
            "The Confirm password field is not right. There should be message about error for do not match password"

        # check field Password on right error message about not match the password
        assert self.reg_page.get_hasError_validation_text_for_field('Password') == prifileObj.valid_for_not_match_password_text, \
            "No validation message for Password and Confirm password fields are do not matched"


        print('---------  SUCCESS test_validation_not_match_passwrd_to_confirm_passwrd -----------')
        driver.quit()


    def test_validation_empty_passwrd_and_not_empty_confirm_passwrd(self):
        """Test for check validation not matched fields Confirm password and password (passwopd is empty, confirm password in not empty)"""
        print('========================================================================')
        print('Test for check validation not matched fields Confirm password and password (passwopd is empty, confirm password in not empty)')

        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        email_registration = prifileObj.get_random_email()

        self.reg_page.fill_name(prifileObj.new_user_date['name'])
        self.reg_page.fill_email(email_registration)
        self.reg_page.fill_confirm_password(prifileObj.new_user_date['not_right_confirm_password'])

        self.reg_page.click_sign_up_btn()

        time.sleep(2)

        # check has field Password error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Password') == True, \
            "The Confirm password field is not right. There should be message about error for do not match password"

        # check field Password on right error message about not match the password
        assert self.reg_page.get_hasError_validation_text_for_field('Password') == prifileObj.valid_requirement_text_for_password, \
            "No validation message for Password that password field is required "


        print('---------  SUCCESS test_validation_empty_passwrd_and_not_empty_confirm_passwrd -----------')
        driver.quit()


    def test_validation_passwrd_length_less_6(self):
        """Test for check validation field password on length less 6"""
        print('========================================================================')
        print('Test for check validation field password on length less 6')

        #Load Registrtion page
        self.reg_page.open_registration_page()
        driver = self.reg_page.driver

        global_m = Global_Methods(driver)

        #cheks if right title
        assert self.reg_page.is_title_matches(), "Registration title page doesn't match"

        prifileObj = RegistrationProfile()

        email_registration = prifileObj.get_random_email()

        self.reg_page.fill_name(prifileObj.new_user_date['name'])
        self.reg_page.fill_email(email_registration)
        self.reg_page.fill_password(prifileObj.password_5_length)
        self.reg_page.fill_confirm_password(prifileObj.password_5_length)

        self.reg_page.click_sign_up_btn()

        time.sleep(2)

        # check has field Password error text
        assert global_m.is_exist_by_xpath(RegistrationPageLocators.HAS_ERROR_FLD_TEXT['valuename'], 'Password') == True, \
            "The password field is not right. There should be message about error that password length have not  be less 6 "

        # check field Password on right error message about ;ength should be 6 and greater
        assert self.reg_page.get_hasError_validation_text_for_field('Password') == prifileObj.valid_for_password_length_less_6, \
            "No validation message for Password that password field length should not be less 6"


        print('---------  SUCCESS test_validation_passwrd_length_less_6 -----------')
        driver.quit()



    def tear_down(self):
        self.reg_page.driver.quit()


if __name__ == "__main__":
    unittest.main()