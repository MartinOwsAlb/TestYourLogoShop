"""
Data filling module that will help to interact with personal data form.
"""
from app.helpers.action import ActionHelper
from app.helpers.randomizer import Randomizer
from app.helpers.wait import WaitHelper
from app.pages_elements.your_personal_info_page import PersonalInformationPage as Per


class PersonalDataFilling:
    @classmethod
    def process_filling(cls, driver):
        WaitHelper.wait_until_xpath_visibility(driver, xpath=Per.MR_TITLE)
        ActionHelper.click_element_by_xpath(driver, xpath=Per.MR_TITLE)
        ActionHelper.insert_data(driver, xpath=Per.FIRST_NAME_CUSTOMER, data="Jacek")
        ActionHelper.insert_data(driver, xpath=Per.LAST_NAME_CUSTOMER, data="Nowak")
        ActionHelper.click_element_by_xpath(driver, xpath=Per.EMAIL)
        ActionHelper.insert_data(driver, xpath=Per.PASSWORD, data="War123")
        ActionHelper.insert_data(driver, xpath=Per.COMPANY, data="Win Company")
        ActionHelper.insert_data(driver, xpath=Per.ADDRESS, data="Zlota 44")
        ActionHelper.insert_data(driver, xpath=Per.CITY, data="Warsaw")
        ActionHelper.select_data_from_select(driver, xpath=Per.STATE, text="Iowa")
        ActionHelper.insert_data(driver, xpath=Per.ZIP_CODE, data="00007")
        ActionHelper.select_data_from_select(driver, xpath=Per.COUNTRY, text="United States")
        ActionHelper.insert_data(driver, xpath=Per.ADDITIONAL_INFO, data=Randomizer.random_str(30))
        ActionHelper.insert_data(driver, xpath=Per.HOME_PHONE, data="444888773")
        ActionHelper.insert_data(driver, xpath=Per.MOBILE_PHONE, data="444888775")
