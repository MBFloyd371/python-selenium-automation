from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from app.application1 import Application
from sap.application_signin import application
from tap.application2 import Application1
def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = \
     webdriver.Chrome(executable_path=r'C:\Users\mbflo\Automation\python-selenium-automation\chromedriver.exe')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)
    context.sap = application(context.driver)
    context.tap = Application1(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()