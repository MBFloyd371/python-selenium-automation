from selenium.webdriver.common.by import By
from Behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click cart')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#nav-cart").click()


