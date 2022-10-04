from selenium import webdriver
from selenium.webdriver.common.by import By

# Incognito Mode
c = webdriver.ChromeOptions()
c.add_argument("--incognito")

# Path Connection
driver = webdriver.Chrome(executable_path=r'C:\Users\floyd2\Automation\python-selenium-automation\chromedriver.exe', options=c)
driver.implicitly_wait(0.5)
driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

#Test Case 1
head_links = driver.find_element(By.CSS_SELECTOR, ".celwidget.c-f")
def verify_link_count(expected_link_count):
    expected_link_count = int(expected_link_count)

    links = driver.find_elements(*head_links)

    assert len(links) == expected_link_count, \
         f'Expected {expected_link_count} links but got {len(links)}'

#Test Case from Homework 3
driver.get('https://www.amazon.com/Starts-Us-Novel-Ends/dp/1668001225/ref=zg_sccl_2/140-6494202-2303451?pd_rd_w=nilD9&content-id=amzn1.sym.193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_p=193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_r=K8A95CCPNBXKY3M61E42&pd_rd_wg=ebv6G&pd_rd_r=4a76d70a-0366-49c6-a915-3f9ce5f7a7eb&pd_rd_i=1668001225&psc=1')
product_number = (By.XPATH, "//div[@id='cart-size']")
driver.find_element(By.CSS_SELECTOR, "#buy-now-button").click()
def verify_results(expected_result):
    actual_result = driver.find_element(*product_number).text
    assert expected_result == actual_result, f'Error Expected {expected_result}, but got {actual_result}'