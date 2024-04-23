# Import configuration settings or fixtures from conftest.py.
import conftest

# Import the By class for locating elements on the web page.
from selenium.webdriver.common.by import By

# Import the BasePage class to inherit common web page interaction functionalities.
from pages.base_page import BasePage


# Class to represent the cart page interactions, inheriting from BasePage.
# CartPage class encapsulates the specific interactions required for managing the cart on the web application's page.
class CartPage(BasePage):

    # Constructor to initialize the CartPage class.
    def __init__(self):

        # Call the constructor of the BasePage to ensure proper initialization.
        super().__init__()

        # Retrieve the global driver instance from conftest.py to be used for this page object.
        self.driver = conftest.driver

        # Define a dynamic locator template for inventory items. The item name will be formatted into this locator as
        # needed.
        self.inventory_item = (By.XPATH, "//*[@class='inventory_item_name' and text()='{}']")

        # Define the locator for the "Continue Shopping" button on the cart page.
        self.continue_shopping_button = (By.ID, "continue-shopping")

    # Checks if the specified product is present in the cart by using a dynamic locator that includes the product name.
    def check_if_product_to_cart_exist(self, item_name):

        # Format the item name into the dynamic locator template.
        item_locator = (self.inventory_item[0], self.inventory_item[1].format(item_name))

        # Use the inherited check_if_element_exist method to assert the visibility of the product in the cart.
        self.check_if_element_exist(item_locator)

    # Clicks the "Continue Shopping" button on the cart page to navigate back to the shopping area.
    def click_continue_shopping_button(self):

        # Use the inherited click method to perform the click action on the "Continue Shopping" button.
        self.click(self.continue_shopping_button)
