class SummaryProcessPage:
    PROCEED_TO_CHECKOUT = "(//span[contains(text(),'Proceed to checkout')])[2]"
    # Sig in tab
    EMAIL_ADDRESS = "//input[@id='email_create']"
    CREATE_AN_ACCOUNT = "//button[@id='SubmitCreate']"
    # Address tab
    MESSAGE_TO_ORDER = "//textarea[@name='message']"
    # Shipping tab
    AGREE_TERMS = "//div[@id='uniform-cgv']"
    # Payment tab
    PAY_BY_BANK_WIRE = "//a[@title='Pay by bank wire']"
    PAY_BY_CHECK = "//a[@title='Pay by check.']"
    CONFIRM_MY_ORDER = "//span[normalize-space()='I confirm my order']"
    ASSERT_MESSAGE = "//strong[normalize-space()='Your order on My Store is complete.']"
