from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

current_color = (By.CSS_SELECTOR, "#variation_color_name .selection")
color_options = (By.CSS_SELECTOR, "#variation_color_name li")


@given('Open Amazon product B07BJKRR25')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@then('Verify That user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black', 'Bright White']

    actual_colors = []

    colors = context.driver.find_element(*color_options)
    print('Colors:', colors)
    for color in colors:
        color.click()
        current_color = context.driver.find_element(*current_color).text
        actual_colors += [current_color]
        print(actual_colors)

    assert expected_colors == actual_colors, \
    f'Expected colors {expected_colors}, but got {actual_colors}'
