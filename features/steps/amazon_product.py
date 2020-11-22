from behave import given, when, then
from selenium.webdriver.common.by import By

@given("Product clothing product page")
def open_product(context):
    context.app.product_page.open_product()

@when("User Hover over New Arrivals")
def hover_arrival(context):
    context.app.product_page.hover_over()

@then("verify Hover Pop up")
def verify_pop_up(context):
    context.app.product_page.verify_hover_pop()