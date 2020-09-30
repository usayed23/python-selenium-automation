from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_Input = (By.ID, 'twotabsearchtextbox')
SEARCH_Icon = (By.XPATH, "//input[@type='submit' and @class='nav-input']")
SEARCH_Result = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input Dress into Amazon search field')
def input_search_word(context):
    context.driver.find_element(*SEARCH_Input).send_keys('Dress')


@when('Click on Amazon search icon')
def click_search_icon(context):
    search_icon = context.driver.find_element(*SEARCH_Icon)
    search_icon.click()

@then('Search results for Dress is shown')
def verify_search_result(context):
    result = context.driver.find_element(*SEARCH_Result)
    assert result.text == '"Dress"', f'Error. Expected Dress1,but got{result.text}'