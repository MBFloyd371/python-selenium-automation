from Pages.cart_page import CartPage

class Application1:
    def __int__(self, driver):
        self.driver = driver
        self.cart_page = CartPage(self.driver)
