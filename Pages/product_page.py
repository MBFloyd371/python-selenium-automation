from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from Pages.Base_Page import Page

class ProductPage(Page):
    orders_click = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    cart_click = (By.CSS_SELECTOR, "#nav-cart")
    All_click = (By.ID, 'nav-search-dropdown-card')
    Tab_SELECTION = (By.XPATH, "//a[@aria-label='New Arrivals']")
    Department_selection = (By.ID, 'search-alias=appliances')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    Menu = (By.XPATH, "//ul[@class='mm-category-list']")

    def open_amazon_product(self, product_id):
        self.driver.get(f'https://www.amazon.com/dp/{product_id}/')




    def hover_section(self):
        tab_selection = self.find_element(*self.Tab_SELECTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab_selection)
        actions.perform()

    def verify_deals(self):
        self.wait_for_element_appear(*self.Tab_SELECTION)
