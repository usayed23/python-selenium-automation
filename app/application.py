from pages.main_page import MainPage
from pages.sign_in_page import VerifySignIn
from pages.cart_page import VerifyCart


class Application:

    def __init__(self,driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.sign_in_page = VerifySignIn(self.driver)
        self.cart_page = VerifyCart(self.driver)