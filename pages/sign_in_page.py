from selenium.webdriver.common.by import By

from pages.base_page import Page

class VerifySignIn(Page):
      VERIFY_SIGN_IN = By.XPATH, "//h1[@class='a-spacing-small']"


      def Verify_Sign_In(self):
          sign_in_verify = self.driver.find_element(*self.VERIFY_SIGN_IN).text
          assert sign_in_verify == 'Sign-In',f'Expected Sign-In but for {sign_in_verify}'
