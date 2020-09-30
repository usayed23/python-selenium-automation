from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\usyed\\PycharmProjects\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# input into search field of Find more Solution
Input_FMS = driver.find_element(By.ID, "helpsearch")

Input_FMS.send_keys("Cancel Order")

# Click go
Input_FMS.send_keys(Keys.ENTER)

# verify "Cancel Items or Orders"
Result_amazon = driver.find_element(By.XPATH, "//h1[contains(text(),'Cancel Items or Orders')]").text

if "Cancel Items or Orders" == Result_amazon:

    print("Test case passed")
else:
    print("Test case failed")