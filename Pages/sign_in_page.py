from Pages.Base_Page import Page

class Signin(Page):
    def verify(self):
        assert self.driver.current_url.find("//h1[@class='a-spacing-small']" and "//input[@type='email']"), f"Expected not in {self.driver.current_url.find()}"