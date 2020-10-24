from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

IMAGE = By.CSS_SELECTOR, 'img.imgSwatch'
COLOR = By.CSS_SELECTOR,'span.selection'


@given("Open Amazon jean's page")
def amazon_jean_pg(context):
    context.driver.get("https://www.amazon.com/gp/product/B07ND8QGKX/?th=1")


@then("Verify user can click on all jean's colors")
def verify_jean_color(context):
    expected_color = ["Black","Blue Overdyed","Dark Wash","Indigo Wash","Light Wash","Medium Wash","Rinse","Vintage Light Wash"]
    image = context.driver.find_elements(*IMAGE)
    colors = context.driver.find_element(*COLOR)

    for x in range(len(image)):
        image[x].click()
        assert colors.text == expected_color[x], f'Color dont match. Expected{expected_color[x]} but got {colors.text}'
