from Pages.sign_in_page import Signin

class application:
    def __int__(self, driver):
        self.driver = driver
        self.main_page = Signin(self.driver)
