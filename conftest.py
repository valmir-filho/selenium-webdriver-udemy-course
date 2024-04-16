# Import the pytest module to use its features for testing.
import pytest

# Import the webDriver module from selenium to interact with web browsers.
from selenium import webdriver

# Declare a global variable to hold the driver object. This type hint specifies that driver will be an instance of a
# Selenium WebDriver.
driver: webdriver.Remote


@pytest.fixture()
def setup_teardown():
    # Declare the use of the global driver variable.
    global driver

    # Set up the Edge browser using WebDriver.
    driver = webdriver.Edge()

    # Maximize the browser window to ensure visibility of all elements.
    driver.maximize_window()

    # Set an implicit wait of 12 seconds to allow elements to load before interacting with them.
    driver.implicitly_wait(12)

    # Navigate to the specified website using the browser.
    driver.get("https://www.saucedemo.com/")

    # Yield control back to the test function. Execution resumes here after the test function has completed.
    yield

    # Close the browser and end the session.
    driver.quit()
