# Import configuration settings or fixtures from conftest.py.
import conftest

# Import BasePage to extend its functionalities.
from pages.base_page import BasePage

# Import the By class for locating elements on the web page.
from selenium.webdriver.common.by import By


# HomePage class extends BasePage, containing specific methods and properties related to the home page of the
# application.
class HomePage(BasePage):

    def __init__(self):

        # Initialize the parent class (BasePage).
        super().__init__()

        # Retrieve the global driver instance from conftest.py to be used for this page object.
        self.driver = conftest.driver

        # Define the locator for the page title element.
        self.page_title = (By.XPATH, "//span[@class='title']")

    # Checks if the login was successful by asserting the visibility of the page title element. This method uses the
    # inherited "check_if_element_exist" method from BasePage to verify the element's presence.
    def check_if_logged_in_successfully(self):

        # Utilize the "check_if_element_exist" method to ensure the page title is displayed.
        self.check_if_element_exist(self.page_title)
