from selenium.webdriver.common.by import By
from Behave import given, when, then

@then('Verify Sign in label visible and email input field present')
def verify_cart(context):
    assert context.driver.current_url.find("//h2[contains(text(), 'Your Amazon')]"), f"Expected not in {driver.current_url.find()}"
