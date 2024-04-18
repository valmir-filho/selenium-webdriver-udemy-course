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

        # Define the locator for the page title element, used to verify if login was successful.
        self.page_title = (By.XPATH, "//span[@class='title']")

        # Define a dynamic locator template for inventory items. The item name will be formatted into this locator as
        # needed.
        self.inventory_item = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']")

        # Define the locator for the "Add to Cart" button associated with items.
        self.add_to_cart_button = (By.XPATH, "//*[text()='Add to cart']")

        # Define the locator for the cart icon, used to navigate to the cart page.
        self.cart_icon = (By.XPATH, "//*[@class='shopping_cart_link']")

    # Verifies that the login was successful by checking the visibility of the page title.
    def check_if_logged_in_successfully(self):

        # Utilize the "check_if_element_exist" method to ensure the page title is displayed.
        self.check_if_element_exist(self.page_title)

    # Adds a specified item to the shopping cart by clicking on the item and the "Add to Cart" button.
    def add_to_cart(self, item_name):

        # Format the item name into the locator and click on the item.
        item_locator = (self.inventory_item[0], self.inventory_item[1].format(item_name))

        self.click(item_locator)

        # Click on the "Add to Cart" button for the item.
        self.click(self.add_to_cart_button)

    # Navigates to the cart page by clicking on the cart icon.
    def access_cart(self):

        # Click on the cart icon to navigate to the cart page.
        self.click(self.cart_icon)
