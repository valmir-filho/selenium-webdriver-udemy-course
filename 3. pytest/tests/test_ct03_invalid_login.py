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
class TestCT03:
    def test_ct03_valid_login(self):
        
        # Retrieve the global driver instance from conftest.py, shared across the pytest tests.
        driver = conftest.driver

        # Locate the username input field by its ID and store it in a variable for user interaction.
        username = driver.find_element(By.ID, "user-name")

        # Enter a predefined username into the input field.
        username.send_keys("standard_user")

        # Pause execution to allow time for the user input to be entered, simulating real user interaction.
        time.sleep(2)

        # Locate the password input field by its ID and store it in a variable.
        password = driver.find_element(By.ID, "password")

        # Enter a password into the input field, which might be incorrect or part of a test case scenario.
        password.send_keys("secret")

        # Pause execution to allow time for the password to be entered, ensuring the application has time to process
        # the input.
        time.sleep(2)
