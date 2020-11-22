from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class AmazonPage(Page):

    DEPARTMENT_DD = (By.ID,"searchDropdownBox")
    SEARCH_FIELD = (By.ID,"twotabsearchtextbox")
    SEARCH_ICON = (By.XPATH, "//input[@type='submit' and @class='nav-input']")

    def open_amazon(self):
        self.open_page('https://www.amazon.com/')


    def select_department(self):

        dd = self.find_element(*self.DEPARTMENT_DD)
        select = Select(dd)
        select.select_by_value('search-alias=videogames')


    def search_for_game_console(self):
        self.input('ps5',*self.SEARCH_FIELD)

    def click_on_search_icon(self):
        self.click(*self.SEARCH_ICON)

