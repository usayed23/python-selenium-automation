from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\usyed\\PycharmProjects\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()


# open the url
driver.get('https://www.amazon.com/')

CLick_Sigin =driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']")

CLick_Sigin.click()






