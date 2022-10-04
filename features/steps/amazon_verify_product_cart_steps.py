from selenium.webdriver.common.by import By
from Behave import given, when, then


product_number = (By.XPATH, "//div[@id='cart-size']")


@then('Verify results has {expected_result} are shown')
def verify_results(context, expected_result):
    actual_result = context.driver.find_element(*product_number).text
    assert expected_result == actual_result, f'Error Expected {expected_result}, but got {actual_result}'



