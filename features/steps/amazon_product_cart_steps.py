from selenium.webdriver.common.by import By
from Behave import given, when, then


@given('Open Amazon Books page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/Starts-Us-Novel-Ends/dp/1668001225/ref=zg_sccl_2/140-6494202-2303451?pd_rd_w=nilD9&content-id=amzn1.sym.193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_p=193afb92-0c19-4833-86f8-850b5ba40291&pf_rd_r=K8A95CCPNBXKY3M61E42&pd_rd_wg=ebv6G&pd_rd_r=4a76d70a-0366-49c6-a915-3f9ce5f7a7eb&pd_rd_i=1668001225&psc=1')


@when('Click preorder now')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "#buy-now-button").click()

