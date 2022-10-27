from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify Cart is empty')
def verify_cart(context):
    #assert context.driver.current_url.find("//h2[contains(text(), 'Your Amazon')]"), f"Expected not in {driver.current_url.find()}"
    context.tap.cart_page.verify()
