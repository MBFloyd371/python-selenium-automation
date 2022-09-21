from selenium import webdriver
from selenium.webdriver.common.by import By

# Incognito Mode
c = webdriver.ChromeOptions()
c.add_argument("--incognito")

# Path Connection
driver = webdriver.Chrome(executable_path=r'C:\Users\floyd2\Automation\python-selenium-automation\chromedriver.exe', options=c)
driver.implicitly_wait(0.5)
driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

# Find XPATH Locators Page Elements
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
driver.find_element(By.XPATH, "//input[@type='email']")
driver.find_element(By.XPATH, "//input[@id='continue']")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

# Find XPATH Locators That Contains Text
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Pri')]")

#Test Case
driver.get("https://www.amazon.com/")
driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
expected_result = driver.current_url.find("//h1[@class='a-spacing-small']" and "//input[@type='email']")
actual_result = driver.current_url.find("//h1[@class='a-spacing-small']" and "//input[@type='email']")
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

# Or Can Be Written As This
assert driver.current_url.find("//h1[@class='a-spacing-small']" and "//input[@type='email']"), f"Expected not in {driver.current_url.find()}"

print("Test Passed")

driver.quit()
