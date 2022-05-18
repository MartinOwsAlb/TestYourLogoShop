import os


class Settings:
    # platform to choose to run remote or local
    RUN_PLATFORM: str = os.environ.get("ACCEPTOR_RUN_PLATFORM")
    SELENIUM_URL: str = os.environ.get("ACCEPTOR_SELENIUM_URL")

    # local path
    MAIN_LOCAL_PATH = os.environ.get("ACCEPTOR_MAIN_LOCAL_PATH")
    PATH_CHROME = os.environ.get("ACCEPTOR_PATH_CHROME", f"/{MAIN_LOCAL_PATH}/local_drivers/chromedriver")
    PATH_FIREFOX = os.environ.get("ACCEPTOR_PATH_FIREFOX", f"/{MAIN_LOCAL_PATH}/local_drivers/geckodriver")
    BROWSERS_LIST = list(os.environ.get("ACCEPTOR_BROWSERS_LIST", "firefox,chrome").split(','))

    # list of urls
    START_URL = os.environ.get("ACCEPTOR_BASE_URL", "http://automationpractice.com/index.php")


SETTINGS = Settings()
# time to wait
DEFAULT_WAIT = 30
