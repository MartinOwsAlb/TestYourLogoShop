import allure
import pytest

from app.helpers.randomizer import Randomizer
from app.test_scenarios.buying_products_flow.base_elements import StartBaseElements


@allure.suite("Test buying product")
class TestBuyingProduct(StartBaseElements):
    """
    Tests of the process of buying one product.
    """

    @pytest.mark.parametrize(
        'product_size',
        [
            "S",
            "M",
            "L"
        ],
        ids=["product size S", "product size M", "product size L"]
    )
    @allure.sub_suite("Test buying one product")
    def test_buying_one_product(self, product_size):
        """
        The test verifies the correct operation to buy one product.
        """
        self._go_to_start_page()
        self._go_to_product_tab()
        self._select_value_and_size(size=product_size)
        self._add_to_card()
        self._proceed_to_checkout()
        self._summary_proceed_to_checkout()
        self._create_an_account(Randomizer.random_email())
        self._process_filling_the_personal_form()
        self._add_order_message_and_go_to_shipping()
        self._agree_terms_and_go_to_payment()
        self._choose_payment_type()
        self._assert_order(product_size=product_size)
