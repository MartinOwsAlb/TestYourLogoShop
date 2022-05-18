class StartPage:
    SLIDER_BANNER = "//div[@id='slider_row']"
    CENTER_COLUMN = "//div[@id='center_column']"
    PRODUCT_QUANTITY = "//input[@id='quantity_wanted']"
    SIZE_SELECT = "//select[@id='group_1']"
    ADD_TO_CARD = "//button[@name='Submit']"
    SUMMARY_CARD = "//div[@id='layer_cart']"
    PROCEED_TO_CHECKOUT = "//a[@title='Proceed to checkout']"

    @classmethod
    def product_place(cls, place):
        return f"(//div[@class='product-container'])[{place}]"
