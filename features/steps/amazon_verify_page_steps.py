from selenium.webdriver.common.by import By
from Behave import given, when, then

@then('Verify Sign in label visible and email input field present')
def verify_page(context):
    expected_text = 'Sign in'
    actual_text = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    assert expected_text == actual_text, f'Error! Expected {expected_text}, but got {actual_text}'

    assert context.driver.current_url.find("//input[@type='email']"), f"Expected not in {driver.current_url.find()}"
