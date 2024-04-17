# Import configuration settings or fixtures from conftest.py.
import conftest


# BasePage serves as a superclass for all page objects within the application. It contains common functionalities and
# utilities that other pages can inherit, reducing code duplication.
class BasePage:

    def __init__(self):

        # Initialize the BasePage class and retrieve the global driver instance from conftest.py.
        self.driver = conftest.driver

    # Find and return a web element using the specified locator.
    def find_element(self, locator):

        # The "*" operator unpacks the locator tuple into arguments for the find_element method.
        return self.driver.find_element(*locator)

    # Find and return a list of web elements using the specified locator.
    def find_elements(self, locator):

        # Unpack the locator tuple into arguments for the find_elements method.
        return self.driver.find_elements(*locator)

    # Send the specified text to a web element identified by the locator.
    def to_write(self, locator, text):

        # Find the element and send the specified text to it.
        self.find_element(locator).send_keys(text)

    # Click on the web element identified by the locator.
    def click(self, locator):

        # Find the element and perform a click action.
        self.find_element(locator).click()

    # Assert that the element is displayed, with a custom error message if not.
    def check_if_element_exist(self, locator):

        assert self.find_element(locator).is_displayed(), f"The element '{locator}' was not found on the screen."
