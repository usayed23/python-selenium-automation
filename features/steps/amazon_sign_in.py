from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open the Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Amazon Sign In')
def click_amazon_order(context):
    click_on_order = context.driver.find_element(By.XPATH, "//a[@id='nav-link-accountList']")
    click_on_order.click()


@then('Verify Sign In page')
def verify_sign_in(context):
    sign_in_verify = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert sign_in_verify == 'Sign-In'
