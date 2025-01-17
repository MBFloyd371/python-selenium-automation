from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
Menu = (By.CSS_SELECTOR, ".mega-menu")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    #context.driver.get(f'https://www.amazon.com/dp/{product_id}/')
    context.app.product_page.open_amazon_product(product_id)



@when('Hover on New Arrivals')
def hover_section(context):
    context.app.product_page.hover_section()


@when('Click add to cart')
#def click_add_to_cart(context):
   # context.driver.find_element(*ADD_TO_CART_BTN).click()
    #sleep(2)


@when('Store product name')
#def get_product_name(context):
    #context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    #print(f'Current product: {context.product_name}')


@then('Verify user can click through colors')
#def verify_can_click_colors(context):
    #expected_colors = ['Black', 'Solid Black', 'Navy']
    #actual_colors = []

    #colors = context.driver.find_elements(*COLOR_OPTIONS)

    #for color in colors[:3]:
        #color.click()
        #current_color = context.driver.find_element(*CURRENT_COLOR).text
        #actual_colors += [current_color]

    #assert expected_colors == actual_colors, \
        #f'Expected colors {expected_colors} did not match actual {actual_colors}'

@then('Verify deals exist')
def verify_deals(context):
    context.app.product_page.verify_deals()