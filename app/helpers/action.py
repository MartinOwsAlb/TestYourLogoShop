"""
Actions module that will help to interact with visible elements on the site.
"""
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotSelectableException,
    NoSuchElementException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from app.helpers.wait import WaitHelper


class ActionHelper:
    """
    Explanation for the case where we have except and then pass.
    It means that the item is not on the page, but it doesn't affect the test execution and failure.
    """

    @classmethod
    def click_element_by_xpath(cls, driver, xpath):
        try:
            element = driver.find_element(By.XPATH, xpath)
            WaitHelper.wait_to_clickable_xpath(driver, xpath)
            element.click()
        except NoSuchElementException:
            pass
        except ElementClickInterceptedException:
            print(f"{xpath} is not working correctly")

    @classmethod
    def get_text_value_by_xpath(cls, driver, xpath):
        try:
            WaitHelper.wait_until_xpath_visibility(driver, xpath)
            return driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            pass
        except:
            print(f"{xpath} is not working correctly")

    @classmethod
    def insert_data(cls, driver, xpath, data):
        try:
            WaitHelper.wait_until_xpath_visibility(driver, xpath)
            input_box = driver.find_element(By.XPATH, xpath)
            input_box.clear()
            input_box.send_keys(data)
        except NoSuchElementException:
            print(f"{xpath} is not working correctly")


    @classmethod
    def select_data_from_select(cls, driver, xpath, text):
        try:
            select = Select(driver.find_element(By.XPATH, xpath))
            select.select_by_visible_text(text)
        except ElementNotSelectableException:
            print(f"{xpath} is not working correctly")

    @classmethod
    def mouse_hover_action(cls, driver, xpath):
        element_to_hover_over = driver.find_element(By.XPATH, xpath)
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()

    @classmethod
    def clear_input(cls, driver, xpath):
        WaitHelper.wait_until_xpath_visibility(driver, xpath)
        element = driver.find_element(By.XPATH, xpath)
        element.send_keys(Keys.SHIFT, Keys.ARROW_UP)
        element.send_keys(Keys.DELETE)

    @classmethod
    def move_to_element(cls, driver, xpath):
        element = driver.find_element(By.XPATH, xpath)
        ActionChains(driver).move_to_element(to_element=element).perform()

    @classmethod
    def scroll_to_element(cls, driver, xpath):
        element = driver.find_element(By.XPATH, xpath)
        try:
            driver.execute_script("return arguments[0].scrollIntoView();", element)
        except:
            print(f'error scrolling down to web element {element}')
