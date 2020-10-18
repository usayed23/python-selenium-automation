from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SEARCH_WORD= By.ID, "twotabsearchtextbox"
SEARCH_BUTTON = By.ID,"nav-search-submit-text"
CART = By.ID,"add-to-cart-button"
CART_COUNT = By.XPATH, "//span[@id='nav-cart-count']"


@when("Input ball into Amazon search field")
def input_search(context):
    context.driver.find_element(*SEARCH_WORD).send_keys("ball")
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(2)


@when("Click on second search result item")
def click_on_item(context):
    context.driver.find_element_by_link_text("Click N' Play Pack of 200 Phthalate Free BPA Free Crush Proof Plastic Ball, Pit Balls - 6 Bright Colors in Reusable and Durable Storage Mesh Bag with Zipper").click()

@when("Add the item to the cart")
def add_item_cart(context):
    context.driver.find_element(*CART).click()
    sleep(2)

@then("Verify if item is in the cart")
def verify_cart_item(context):
    amazon_cart_count = context.driver.find_element(*CART_COUNT).text

    assert amazon_cart_count == "1", f'Expected 1 but got {amazon_cart_count}'
