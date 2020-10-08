from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


HELP_SEARCH = (By.ID, "helpsearch")
SEARCH_WORD = (By.XPATH, "//h1[contains(text(),'Cancel Items or Orders')]")

# open the url
@given("Open the Help Amazon page")
def open_help_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


# input into search field of Find more Solution and Click Enter
@when("Search for 'Cancel Order'")
def search_cancel_order(context):
    # input into search field of Find more Solution
    input_fms = context.driver.find_element(*HELP_SEARCH)

    input_fms.send_keys("Cancel Order")
    #click go
    input_fms.send_keys(Keys.ENTER)

# verify "Cancel Items or Orders"
@then("Verify 'Cancel items or Orders' page")
def verify_cancel_order(context):
    result_amazon = context.driver.find_element(*SEARCH_WORD).text
    assert result_amazon == 'Cancel Items or Orders', f'Expected "Cancel Items or Orders", but got{result_amazon}'
