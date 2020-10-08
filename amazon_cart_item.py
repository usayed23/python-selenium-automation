from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\\Users\\usyed\\PycharmProjects\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()


# open the url
driver.get('https://www.amazon.com/')

#input search key word
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("ball")

#click on search
driver.find_element(By.ID,"nav-search-submit-text").click()

sleep(3)

#click on the item of choice
driver.find_element_by_link_text("Click N' Play Pack of 200 Phthalate Free BPA Free Crush Proof Plastic Ball, Pit Balls - 6 Bright Colors in Reusable and Durable Storage Mesh Bag with Zipper").click()

#click add to cart
driver.find_element(By.ID,"add-to-cart-button").click()

sleep(2)

#verify cart is showing number of Item
amazon_cart_count = driver.find_element(By.XPATH,"//span[@id='nav-cart-count']").text

assert amazon_cart_count == "1",f'Expected 1 but got {amazon_cart_count}'