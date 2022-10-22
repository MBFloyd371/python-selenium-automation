from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

privacy_link = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")

@given('Open Amazon T&C page')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original: ', context.original_window)


@when('Click on Amazon Privacy Notice link')
def click_link(context):
    context.driver.find_element(*privacy_link).click()


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.current_window_handles
    print('Current windowS: ', current_windows)
    context.driver.switch_to.window(current_windows[1])






