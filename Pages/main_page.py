from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from Pages.Base_Page import Page

class MainPage(Page):
    orders_click = (By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    cart_click = (By.CSS_SELECTOR, "#nav-cart")
    All_click = (By.ID, 'nav-search-dropdown-card')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    Department_selection = (By.ID, 'search-alias=appliances')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')


    def open_url(self):
        self.driver.get('https://www.amazon.com/')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.driver.find_element(*self.orders_click).click()

    def click_cart(self):
        self.driver.find_element(*self.cart_click).click()

    def click_all(self):
        self.driver.find_element(*self.All_click).click()

    def hover_department(self):
        department_selection = self.find_element(*self.DEPARTMENT_SELECTION)
        actions = ActionChains(self.driver)
        actions.move_to_element(department_selection)
        actions.perform()

    def select_department(self, selection_value):
        select = Select(self.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value(f'search-alias={selection_value}')
        #self.driver.find_element(*self.Department_selection).click()










