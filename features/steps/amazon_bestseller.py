from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

FIRST_LINK = By.CSS_SELECTOR, "li.zg_selected"
SECOND_LINK = By.XPATH, "//a[text()='New Releases']"
THIRD_LINK = By.XPATH,"//a[text()='Movers & Shakers']"
FOURTH_LINK = By.XPATH,"//a[text()='Most Wished For']"
FIFTH_LINK = By.XPATH,"//a[text()='Gift Ideas']"


@given("Open Amazon Best Seller")
def amazon_bestseller(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")
    sleep(2)


@then("Verify all links")
def click_on_link(context):

    first_link = context.driver.find_element(*FIRST_LINK)
    first_link.click()
    context.driver.back()
    sleep(4)

    second_link = context.driver.find_elements(*SECOND_LINK)[1]
    second_link.click()
    context.driver.back()
    sleep(4)

    third_link = context.driver.find_element(*THIRD_LINK)
    third_link.click()
    context.driver.back()
    sleep(4)

    fourth_link = context.driver.find_element(*FOURTH_LINK)
    fourth_link.click()
    context.driver.back()
    sleep(4)

    fifth_link = context.driver.find_element(*FIFTH_LINK)
    fifth_link.click()
    context.driver.back()
    sleep(4)