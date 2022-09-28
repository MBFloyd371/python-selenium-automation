from selenium import webdriver
from selenium.webdriver.common.by import By

# Incognito Mode
c = webdriver.ChromeOptions()
c.add_argument("--incognito")

# Path Connection
driver = webdriver.Chrome(executable_path=r'C:\Users\floyd2\Automation\python-selenium-automation\chromedriver.exe', options=c)
driver.implicitly_wait(0.5)
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=00J08GQVR2NF0110G8DY&openid.assoc_handle=usflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Find CSS Locators Page Elements
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo, .a-spacing-small, a.a-link-emphasis")
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name, #ap_email, #ap_password_check")
driver.find_element(By.CSS_SELECTOR, "#ap_password, .a-alert-content")
driver.find_element(By.CSS_SELECTOR, "#continue")
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#Test Case 1
driver.get("https://www.amazon.com/")
driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_text == actual_text, f'Error! Expected {expected_text}, but got {actual_text}'

assert driver.current_url.find("//input[@type='email']"), f"Expected not in {driver.current_url.find()}"

#Test Case 2
driver.get("https://www.amazon.com/")
driver.find_element(By.CSS_SELECTOR, "#nav-cart").click()
assert driver.current_url.find("//h2[contains(text(), 'Your Amazon')]"), f"Expected not in {driver.current_url.find()}"
print("Test Passed")
driver.quit()