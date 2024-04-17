# Import configuration settings or fixtures from conftest.py.
import conftest

# Import the pytest library for creating test cases.
import pytest

# Import the LoginPage class from the "pages" directory to facilitate login.
from pages.login_page import LoginPage

# Import the By class for locating elements.
from selenium.webdriver.common.by import By


# Marks the class to use a specific pytest fixture for setup and teardown processes.
@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_add_products_to_cart(self):

        # Retrieve the global driver instance from conftest.py.
        driver = conftest.driver

        # Create an instance of the LoginPage class to handle login operations.
        login_page = LoginPage()

        # Use the login page to perform the login operation using standard credentials.
        login_page.do_login("standard_user", "secret_sauce")

        # Navigate to the product page for "Sauce Labs Backpack" by clicking on the product name.
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()

        # Add the selected item "Sauce Labs Backpack" to the shopping cart.
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Navigate to the shopping cart page to view the items added to the cart.
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

        # Assert that the "Sauce Labs Backpack" is correctly displayed in the shopping cart.
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name'"
                                             "and text()='Sauce Labs Backpack']").is_displayed()

        # Click on "continue shopping" to return to the product listing page.
        driver.find_element(By.ID, "continue-shopping").click()

        # Navigate to the product page for "Sauce Labs Bike Light" by clicking on its name.
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name '"
                                      "and text()='Sauce Labs Bike Light']").click()

        # Add the "Sauce Labs Bike Light" to the shopping cart.
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Navigate back to the shopping cart to view all the selected items.
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

        # Assert that both the "Sauce Labs Backpack" and "Sauce Labs Bike Light" are displayed in the cart,
        # verifying that multiple items can be successfully added to the shopping cart.
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name'"
                                             "and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name'"
                                             "and text()='Sauce Labs Bike Light']").is_displayed()
