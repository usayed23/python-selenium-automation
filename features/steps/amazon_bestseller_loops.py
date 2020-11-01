from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



ALL_LINKS = (By.ID,'zg_tabs')


@then("Verify all 5 links")
def verify_all_links(context):
     all_links = context.driver.find_elements(*ALL_LINKS)
     print(len(all_links))


     for x in all_links:
         context.driver.wait.until(EC.element_to_be_clickable)
         x.click()
         context.driver.back()
