# Import configuration settings or fixtures from conftest.py.
import conftest
# Import the pytest library for creating test cases.
import pytest
# Import the time library for controlling execution timing.
import time

# Import the By class for locating elements.
from selenium.webdriver.common.by import By


# Marks the class to use a specific pytest fixture for setup and teardown processes.
@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_ct02_valid_login(self):

        # Retrieve the driver instance from the conftest module, which is shared across tests.
        driver = conftest.driver

        # Locate the username input field by its ID and store it in a variable for further actions.
        username = driver.find_element(By.ID, "user-name")

        # Enter the predetermined username into the input field.
        username.send_keys("standard_user")

        # Pause execution to simulate a realistic typing speed and allow time for the interface to respond.
        time.sleep(2)

        # Locate the password input field by its ID, similar to how the username was located.
        password = driver.find_element(By.ID, "password")

        # Enter the corresponding password for the username into the input field.
        password.send_keys("secret_sauce")

        # Pause execution to simulate a realistic typing speed and ensure the password is processed correctly.
        time.sleep(2)

        # Locate the login button by its ID to proceed with the authentication.
        login_button = driver.find_element(By.ID, "login-button")

        # Click on the login button to submit the login form with the credentials provided.
        login_button.click()

        # Pause execution to allow time for the server to process the login and navigate to the next page.
        time.sleep(2)

        # Assert that the Products page title is displayed after logging in, ensuring the login was successful.
        # This serves as a verification step to confirm that the user has reached the intended page after login.
        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()
