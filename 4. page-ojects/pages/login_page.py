# Import configuration settings or fixtures from conftest.py.
import conftest

# Import the By class for locating elements on the web page.
from selenium.webdriver.common.by import By

# Import the BasePage class to inherit common web page interaction functionalities.
from pages.base_page import BasePage


# Class to represent the login page interactions, inheriting from BasePage.
# LoginPage class that encapsulates the specific interactions required to perform login actions on the web
# application's login page.
class LoginPage(BasePage):

    # Constructor to initialize the LoginPage class.
    def __init__(self):

        # Call the constructor of the BasePage to ensure proper initialization.
        super().__init__()

        # Retrieve the global driver instance from conftest.py to be used for this page object.
        self.driver = conftest.driver

        # Define locators for the username field, password field, and login button.
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

        # Define locator for the error message that appears after a failed login attempt.
        self.error_message_login = (By.XPATH, "//*[@data-test='error']")

    # Method to perform login using the provided username and password.
    # Perform login using the specified username and password by entering the credentials into the form and submitting
    # it.
    def do_login(self, username, password):

        # Use the inherited to_write method from BasePage to enter the username into the username field.
        self.to_write(self.username_field, username)

        # Use the inherited to_write method from BasePage to enter the password into the password field.
        self.to_write(self.password_field, password)

        # Use the inherited click method from BasePage to click the login button and submit the login form.
        self.click(self.login_button)

    # Check if the error message is displayed after a failed login attempt. This method uses the inherited
    # "check_if_element_exist" method from BasePage to verify the element's presence.
    def check_error_message_login(self):

        # Utilize the "check_if_element_exist" method to ensure the error message is displayed on unsuccessful login.
        self.check_if_element_exist(self.error_message_login)
