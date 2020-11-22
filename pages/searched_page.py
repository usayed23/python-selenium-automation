from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class VerifyDepartment(Page):

    VERIFY_DEPT = (By.XPATH ,"//span[text()='Video Games']")

    def verify_department(self):
        verify_departmemt = self.driver.find_element(*self.VERIFY_DEPT).text
        assert verify_departmemt == 'Video Games', f'Expected Video Games but for {verify_departmemt}'
