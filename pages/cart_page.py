from selenium.webdriver.common.by import By

from pages.base_page import Page

class VerifyCart(Page):
    VERIFY_CART = By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]"


    def verifyCart(self):
        result_cart = self.driver.find_element(*self.VERIFY_CART).text
        assert result_cart == "Your Amazon Cart is empty", f'Expected Your Amazon Cart is empty, but got {result_cart}'


