from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Sign in is opened')
def verify(context):
    #assert context.driver.current_url.find("//h1[@class='a-spacing-small']" and "//input[@type='email']"), f"Expected not in {context.driver.current_url.find()}"
    context.sap.sign_in_page.verify()