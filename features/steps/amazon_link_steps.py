from selenium.webdriver.common.by import By
from Behave import given, when, then

head_links = driver.find_element(By.CSS_SELECTOR, ".celwidget.c-f")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify That Header has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)

    links = context.driver.find_elements(*head_links)

    assert len(links) == expected_link_count, \
         f'Expected {expected_link_count} links but got {len(links)}'


