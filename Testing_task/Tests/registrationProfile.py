# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import choice
from string import ascii_lowercase


class RegistrationProfile(object):
    new_user_date = {
        'name': 'Ivan',
        'email': 'aaa@fff.kkk',
        'password': 'passwo',
        'confirm_password':  'passwo',
        'not_right_confirm_password': 'ppaassww',
    }

    count_registration_hasError_fields = 3

    count_registration_hasError_fields_entering_existing_email = 1

    valid_requirement_text_for_name = 'The name field is required.'
    valid_requirement_text_for_email = 'The email field is required.'
    valid_requirement_text_for_password = 'The password field is required.'
    valid_requirement_text_for_confirm_password = 'The confirm password field is required.'


    #values for testing the validation Name field

    name_255_length = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234568901111111111222222222233333333334444444444555555555566666666667777777777888888888899999999990000000000ddddddddddhhhhhhhhhhffffffffffeeeeeeeeeeemmmmmmmmmm12345'
    name_256_length = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234568901111111111222222222233333333334444444444555555555566666666667777777777888888888899999999990000000000ddddddddddhhhhhhhhhhffffffffffeeeeeeeeeeemmmmmmmmmm123456'
    name_with_different_characters = '~`!@№#&;%:*()_+.?/=^_{|}<>'
    name_with_capital_letters = 'ABRA CADABRA BIG LETTERS'
    name_with_cirillic_letters = 'Абра кадабра кириллица ЭЪЫ ЇТІЄ'
    name_with_one_letter = 'h'

    # values for testing the validation Email field - not right
    email_without_dog = 'myEmailkkk.hhh'
    email_without_point = 'myEmail@kkkhhh'
    email_with_max_length_greater_64_befor_dog = 'qqqqqqqqqqwwwwwwwwwweeeeeeeeeerrrrrrrrrrttttttttttvvvvvvhmmmmmmmz@ddd.fff'
    # values for testing the validation Email field - right
    email_with_capital_letters = 'MYEMAIL@KKK.HHH'
    email_with_numbers_befor_dog = '33344@ddd.sss'
    email_with_numbers_after_dog = 'ddd@123.sss'
    email_with_other_characters_befor_dog = '!#$%`*+-/=?^_{|}~ss@fff.ddd'
    email_with_point_befor_dog = 'Petor.John@ddd.sss'
    email_with_max_length_64_befor_dog = 'qqqqqqqqqqwwwwwwwwwweeeeeeeeeerrrrrrrrrrttttttttttvvvvvvmmmmmmmz@ddd.fff'
    #    '1234567890123456789012345689012345678901234567890@derwerrdd.sss'


    #validation text when entering existing email

    valid_exist_for_email_text = 'The email has already been taken.'

    # validation text when entering not valid email
    no_valid_for_email_text = 'The email must be a valid email address.'

    # validation text when entering name more 255 chars

    valid_for_long_name_text = 'The name may not be greater than 255 characters.'

    #validation text when entering not match password

    valid_for_not_match_password_text = 'The password confirmation does not match.'

    # validation text when entering password with length less 6

    valid_for_password_length_less_6 = 'The password must be at least 6 characters.'

    # validation text when entering password with length less 6



    #values for testing the validation Password field

    name_255_length = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234568901111111111222222222233333333334444444444555555555566666666667777777777888888888899999999990000000000ddddddddddhhhhhhhhhhffffffffffeeeeeeeeeeemmmmmmmmmm12345'
    name_256_length = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234568901111111111222222222233333333334444444444555555555566666666667777777777888888888899999999990000000000ddddddddddhhhhhhhhhhffffffffffeeeeeeeeeeemmmmmmmmmm123456'
    password_5_length = 'asdfg'
    password_6_length = '123456'
    name_with_capital_letters = 'ABRA CADABRA BIG LETTERS'


    def get_random_email(self):
        part1 = (''.join(choice(ascii_lowercase) for i in range(5)))
        part2 = (''.join(choice(ascii_lowercase) for i in range(4)))
        part3 = (''.join(choice(ascii_lowercase) for i in range(3)))
        email = part1+'@'+ part2+ '.'+ part3
        return email


