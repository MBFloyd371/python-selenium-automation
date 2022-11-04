from selenium.webdriver.common.by import By
from behave import given, when, then

#orders_click = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
#All_click = (By.CSS_SELECTOR, "#nav-search-dropdown-card")
DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')

@given('Open Amazon page')
def open_url(context):
    context.app.main_page.open_url()


@when('Click orders')
def click_orders(context):
    #context.driver.find_element(*orders_click).click()
    context.app.main_page.click_orders()


@when('Click All dropdown box')
def click_all(context):
    #context.driver.find_element(*All_click).click()
    context.app.main_page.click_all()


@when('Hover over department options')
def hover_department(context):
    context.app.main_page.hover_department()


@when('Select department by value {selection_value}')
def select_department(context, selection_value):
    context.app.main_page.select_department(selection_value)

@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search_product(product)

@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.search_results_page.verify_department(department)





