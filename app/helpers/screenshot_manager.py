"""
Screenshot manager help to take screenshot from test and save it in screenshot catalog.
"""
import time

from settings import SETTINGS


class ScreenshotListener:

    @classmethod
    def make_screenshot(cls, driver, data):
        driver.save_screenshot(filename=f"{SETTINGS.MAIN_LOCAL_PATH}/screenshot/Order{time.asctime()}.png")
        print(f"Screenshot saved as {data}{time.asctime()}")
