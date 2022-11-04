from Pages.sign_in_page import Signin
from Pages.main_page import MainPage
from Pages.cart_page import CartPage
from Pages.search_results_page import SearchResultsPage
from Pages.product_page import ProductPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.sign_in_page = Signin(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)