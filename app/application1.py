from Pages.main_page import MainPage

class Application:
    def __int__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
