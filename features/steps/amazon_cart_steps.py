from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get('https://www.amazon.com/')
    context.tap.cart_page.open_amazon()


@when('Click cart')
def click_cart(context):
    #context.driver.find_element(By.CSS_SELECTOR, "#nav-cart").click()
    context.tap.cart_page.click_cart()


