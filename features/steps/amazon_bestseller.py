from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given("Open Amazon Best Seller")
def amazon_bestseller(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")
    sleep(2)


@then("Verify all links")
def click_on_link(context):

    first_link = context.driver.find_element(By.CSS_SELECTOR, "li.zg_selected")
    first_link.click()
    context.driver.back()
    sleep(4)

    second_link = context.driver.find_elements(By.XPATH, "//a[text()='New Releases']")[1]
    second_link.click()
    context.driver.back()
    sleep(4)

    third_link = context.driver.find_element(By.XPATH,"//a[text()='Movers & Shakers']")
    third_link.click()
    context.driver.back()
    sleep(4)

    fourth_link = context.driver.find_element(By.XPATH,"//a[text()='Most Wished For']")
    fourth_link.click()
    context.driver.back()
    sleep(4)

    fifth_link = context.driver.find_element(By.XPATH,"//a[text()='Gift Ideas']")
    fifth_link.click()
    context.driver.back()
    sleep(4)