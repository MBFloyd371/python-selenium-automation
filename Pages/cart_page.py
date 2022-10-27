from selenium.webdriver.common.by import By
from Pages.Base_Page import Page

class CartPage(Page):
    def verify_cart(self):
        assert self.driver.current_url.find("//h2[contains(text(), 'Your Amazon')]"), f"Expected not in {self.driver.current_url.find()}"
