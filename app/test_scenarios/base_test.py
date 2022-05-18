import os

import pytest
from selenium import webdriver

from settings import SETTINGS


class BaseTestClass:
    FIREFOX_BROWSER = 'firefox'
    CHROME_BROWSER = 'chrome'

    @pytest.fixture(params=SETTINGS.BROWSERS_LIST, autouse=True)
    def setup(self, request):
        if SETTINGS.RUN_PLATFORM == "local":
            self._local_init_driver(request.param)
        else:
            self._remote_init_driver(request.param)
        yield
        self._teardown_driver()

    def _local_init_driver(self, browser_type):
        # local test run path
        if browser_type == self.CHROME_BROWSER:
            chrome_options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(options=chrome_options, executable_path=SETTINGS.PATH_CHROME,
                                           service_log_path=os.devnull)
        else:
            firefox_options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(options=firefox_options, executable_path=SETTINGS.PATH_FIREFOX,
                                            service_log_path=os.devnull)

    def _remote_init_driver(self, browser_type):
        # selenium hub docker test run path
        url = SETTINGS.SELENIUM_URL
        if browser_type == self.FIREFOX_BROWSER:
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Remote(command_executor=url, options=options)
        elif browser_type == self.CHROME_BROWSER:
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Remote(command_executor=url, options=options)

    def _teardown_driver(self):
        self.driver.quit()
