from behave import given, when, then
from selenium.webdriver.common.by import By

CLICK_CART = (By.ID,"nav-cart")
VERIFY_CART = (By.XPATH,"//h2[contains(text(),'Your Amazon Cart is empty')]")

@given('Open the Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

@when("Click on the cart icon")
def click_cart(context):
    context.driver.find_element(*CLICK_CART).click()

@then("Verify cart is empty")
def verify_cart(context):
    result_cart = context.driver.find_element(*VERIFY_CART).text
    assert result_cart =="Your Amazon Cart is empty", f'Expected Your Amazon Cart is empty, but got {result_cart}'
