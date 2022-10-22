from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('Verify Amazon Privacy Notice page is opened')
def verify_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/display.html'))
    print('Current Window: ', context.driver.current_window_handle)


@then('User can close new window')
def close_window(context):
    context.driver.close()


@then('Switch back to original')
def return_to_original(context):
    context.driver.switch_to.window(context.original_window)

