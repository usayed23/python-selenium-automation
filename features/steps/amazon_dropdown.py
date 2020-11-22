from behave import given, when, then
from selenium.webdriver.common.by import By



@when("User selects the video games department")
def select_department(context):
    context.app.amazon_page.select_department()

@when("User searches for PS5 in chosen department")
def search_for_game(context):
    context.app.amazon_page.search_for_game_console()

@then("User Verifies that chosen department is searched in")
def verify_dept(context):
    context.app.searched_page.verify_department()