from behave import given, when, then
from selenium.webdriver.common.by import By

CLICK_CART = (By.ID,"nav-cart")
VERIFY_CART = (By.XPATH,"//h2[contains(text(),'Your Amazon Cart is empty')]")

@given('Open the Amazon page')
def open_amazon(context):
    context.app.main_page.open_amazon()

@when("Click on the cart icon")
def click_cart(context):
    context.app.main_page.click_on_the_cart_icon()

@then("Verify cart is empty")
def verify_cart(context):
    context.app.cart_page.verifyCart()
