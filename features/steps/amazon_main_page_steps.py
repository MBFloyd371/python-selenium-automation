from selenium.webdriver.common.by import By
from behave import given, when, then

#orders_click = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")

@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_amazon()




@when('Click orders')
def click_orders(context):
    #context.driver.find_element(*orders_click).click()
    context.app.main_page.click_orders()


