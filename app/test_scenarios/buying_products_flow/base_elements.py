import allure

from app.helpers import (
    ActionHelper,
    PersonalDataFilling,
    Randomizer,
    ScreenshotListener,
    WaitHelper,
)
from app.pages_elements import (
    PersonalInformationPage,
    StartPage,
    SummaryProcessPage,
)
from settings import SETTINGS
from app.test_scenarios.base_test import BaseTestClass


class StartBaseElements(BaseTestClass):

    @allure.step("Go to start page")
    def _go_to_start_page(self):
        self.driver.get(SETTINGS.START_URL)
        WaitHelper.wait_until_xpath_visibility(self.driver, xpath=StartPage.SLIDER_BANNER)

    @allure.step("Go to product tab")
    def _go_to_product_tab(self):
        number_place_xpath = StartPage.product_place(place=Randomizer.random_number_between(down_range=1,
                                                                                            up_range=7))
        ActionHelper.scroll_to_element(self.driver, xpath=number_place_xpath)
        ActionHelper.mouse_hover_action(self.driver, xpath=number_place_xpath)
        ActionHelper.click_element_by_xpath(self.driver, xpath=number_place_xpath)

    @allure.step("Select value and size of product")
    def _select_value_and_size(self, size):
        ActionHelper.insert_data(self.driver, xpath=StartPage.PRODUCT_QUANTITY, data=Randomizer.random_value())
        ActionHelper.select_data_from_select(self.driver, xpath=StartPage.SIZE_SELECT, text=size)

    @allure.step("Add to card product")
    def _add_to_card(self):
        ActionHelper.click_element_by_xpath(self.driver, xpath=StartPage.ADD_TO_CARD)
        WaitHelper.wait_until_xpath_visibility(self.driver, xpath=StartPage.SUMMARY_CARD)

    @allure.step("Proceed to checkout")
    def _proceed_to_checkout(self):
        ActionHelper.click_element_by_xpath(self.driver, xpath=StartPage.PROCEED_TO_CHECKOUT)
        WaitHelper.wait_for_url_contains(self.driver, string="order")

    @allure.step("Summary proceed to checkout")
    def _summary_proceed_to_checkout(self):
        ActionHelper.click_element_by_xpath(self.driver, xpath=SummaryProcessPage.PROCEED_TO_CHECKOUT)

    @allure.step("Create an account")
    def _create_an_account(self, email):
        ActionHelper.insert_data(self.driver, xpath=SummaryProcessPage.EMAIL_ADDRESS, data=email)
        ActionHelper.click_element_by_xpath(self.driver, xpath=SummaryProcessPage.CREATE_AN_ACCOUNT)

    @allure.step("Filling the personal form")
    def _process_filling_the_personal_form(self):
        PersonalDataFilling.process_filling(driver=self.driver)
        ActionHelper.click_element_by_xpath(self.driver, xpath=PersonalInformationPage.REGISTER)

    @allure.step("Add order message and go to shipping")
    def _add_order_message_and_go_to_shipping(self):
        ActionHelper.insert_data(self.driver, xpath=SummaryProcessPage.MESSAGE_TO_ORDER, data="Add to order extra bag")
        ActionHelper.click_element_by_xpath(self.driver, xpath=SummaryProcessPage.PROCEED_TO_CHECKOUT)

    @allure.step("Agree terms and go to payment")
    def _agree_terms_and_go_to_payment(self):
        WaitHelper.wait_to_clickable_xpath(self.driver, xpath=SummaryProcessPage.AGREE_TERMS)
        ActionHelper.click_element_by_xpath(self.driver, xpath=SummaryProcessPage.AGREE_TERMS)
        ActionHelper.click_element_by_xpath(self.driver, xpath=SummaryProcessPage.PROCEED_TO_CHECKOUT)

    @allure.step("Choose payment type")
    def _choose_payment_type(self):
        ActionHelper.click_element_by_xpath(self.driver, xpath=SummaryProcessPage.PAY_BY_BANK_WIRE)
        ActionHelper.click_element_by_xpath(self.driver, xpath=SummaryProcessPage.CONFIRM_MY_ORDER)

    @allure.step("Check correct order process")
    def _assert_order(self, product_size):
        msg = ActionHelper.get_text_value_by_xpath(self.driver, xpath=SummaryProcessPage.ASSERT_MESSAGE)
        if msg == "Your order on My Store is complete.":
            ScreenshotListener.make_screenshot(self.driver, data=product_size)
            assert True
        else:
            print("Test Failed order not completed")
            ScreenshotListener.make_screenshot(self.driver, data=product_size)
            assert False
