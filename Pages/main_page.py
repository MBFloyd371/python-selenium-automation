from selenium.webdriver.common.by import By
from Pages.Base_Page import Page

class MainPage(Page):
    orders_click = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")

    def open_amazon(self):
        self.driver.get('https://www.amazon.com/')

    def click_orders(self):
        self.driver.find_element(*self.orders_click).click()
