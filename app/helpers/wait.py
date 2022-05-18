"""
Action module to help wait for elements to be visible on the page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from settings import DEFAULT_WAIT


class WaitHelper:
    @staticmethod
    def wait_until_xpath_visibility(driver, xpath):
        return WebDriverWait(driver, timeout=DEFAULT_WAIT).until(
            expected_conditions.visibility_of_element_located((By.XPATH, xpath)),
            message=f"Element ({xpath}) is not visible")

    @staticmethod
    def wait_invisibility_xpath(driver, xpath):
        return WebDriverWait(driver, timeout=DEFAULT_WAIT).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, xpath)),
            message=f"Element ({xpath}) did not disappear")

    @staticmethod
    def wait_to_clickable_xpath(driver, xpath):
        return WebDriverWait(driver, timeout=DEFAULT_WAIT).until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath)),
            message=f"Element ({xpath}) is not clickable")

    @classmethod
    def wait_for_url_contains(cls, driver, string):
        return WebDriverWait(driver, timeout=DEFAULT_WAIT).until(
            expected_conditions.url_contains(string),
            message=f"No substring ({string}) in url")
