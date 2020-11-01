from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINK = By.XPATH,"//a[text()='Amazon applications']"

@given("Open Amazon T&C page")
def open_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when("Store original windows")
def original_window(context):

    context.original_window = context.driver.current_window_handle


@when("Click on Amazon applications link")
def app_link(context):
    link = context.driver.find_element(*LINK)
    link.click()
    context.i=0
    context.i += 1

@when("Switch to the newly opened window")
def new_page(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.all_windows = context.driver.window_handles
    context.driver.switch_to.window(context.all_windows[context.i])



@then("Amazon app page is opened")
def amazon_window_verification(context):
    assert context.driver.title == "Amazon Mobile Shopping Apps", f'Expected Amazon Mobile Shopping Apps but got {context.driver.title} instead'


@then("User can close new window and switch back to original")
def back_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
    assert context.driver.title == "Amazon.com Help: Conditions of Use", f'Expected Amazon.com Help: Conditions of Use but got {context.driver.title()} instead'

