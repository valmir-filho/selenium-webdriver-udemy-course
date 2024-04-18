# Import configuration settings or fixtures from conftest.py.
import conftest

# Import necessary modules from selenium for advanced web element interactions and key operations.
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.ui import WebDriverWait


# BasePage serves as a superclass for all page objects within the application. It contains common functionalities and
# utilities that other pages can inherit, reducing code duplication.
class BasePage:

    def __init__(self):

        # Initializes the BasePage class and retrieves the global driver instance from conftest.py.
        self.driver = conftest.driver

    def find_element(self, locator):

        # Finds and returns a web element using the specified locator.
        return self.driver.find_element(*locator)

    def find_elements(self, locator):

        # Finds and returns a list of web elements using the specified locator.
        return self.driver.find_elements(*locator)

    def to_write(self, locator, text):

        # Sends the specified text to a web element identified by the locator.
        self.find_element(locator).send_keys(text)

    def click(self, locator):

        # Clicks on the web element identified by the locator.
        self.find_element(locator).click()

    def check_if_element_exist(self, locator):

        # Asserts that the element is displayed.
        assert self.find_element(locator).is_displayed(), f"The element '{locator}' was not found on the screen."

    def get_text_element(self, locator):

        # Waits for an element to appear
        self.wait_for_element_to_appear(locator)

        # Returns it´s text.
        return self.find_element(locator).text

    def wait_for_element_to_appear(self, locator, timeout=10):

        # Waits until the element specified by the locator appears within the given timeout.
        return WebDriverWait(self.driver, timeout).until(e_c.presence_of_element_located(locator))

    def verify_if_element_exist(self, locator):

        # Verifies the existence of an element.
        assert self.find_element(locator), f"Non-existent element {locator}, but is expected to exist."

    def verify_if_element_not_exist(self, locator):

        # Verifies that an element does not exist.
        assert len(self.find_elements(locator)) == 0, f"Existent element {locator}, but is expected not to exist."

    def double_click(self, locator):

        # Performs a double click on the specified element.
        element = self.wait_for_element_to_appear(locator)

        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):

        # Performs a right-click on the specified element.
        element = self.wait_for_element_to_appear(locator)

        ActionChains(self.driver).context_click(element).perform()

    def press_key(self, locator, key):

        # Sends a specific key press to the specified element.
        elem = self.find_element(locator)

        # Map specific key actions to corresponding Selenium Keys.
        key_actions = {
            "ENTER": Keys.ENTER,
            "SPACE": Keys.SPACE,
            "F1": Keys.F1
        }

        elem.send_keys(key_actions.get(key, ''))
