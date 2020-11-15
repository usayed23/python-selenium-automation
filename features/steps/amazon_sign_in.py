from behave import given, when, then
from selenium.webdriver.common.by import By

SIGN_IN = By.XPATH, "//a[@id='nav-link-accountList']"
VERIFY_SIGN_IN = By.XPATH, "//h1[@class='a-spacing-small']"

@given(' Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_amazon()


@when('Click on Amazon Sign In')
def click_amazon_order(context):
    context.app.main_page.click_amazon_order()

@then('Verify Sign In page')
def verify_sign_in(context):
    context.app.sign_in_page.Verify_Sign_In()
