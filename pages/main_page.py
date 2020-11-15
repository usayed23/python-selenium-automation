from selenium.webdriver.common.by import By

from pages.base_page import Page



class MainPage(Page):
    SIGN_IN = By.XPATH, "//a[@id='nav-link-accountList']"
    VERIFY_SIGN_IN = By.XPATH, "//h1[@class='a-spacing-small']"
    CLICK_CART = By.ID, "nav-cart"
    VERIFY_CART = By.XPATH, "//h2[contains(text(),'Your Amazon Cart is empty')]"

    def open_amazon(self):
        self.open_page('https://www.amazon.com/')

    def click_amazon_order(self):
        self.wait_for_element_click(*self.SIGN_IN)

    def click_on_the_cart_icon(self):
        self.click(*self.CLICK_CART)

