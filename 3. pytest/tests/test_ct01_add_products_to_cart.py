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
class TestCT01:
    def test_ct01_add_products_to_cart(self):

        # Retrieve the global driver instance from conftest.py
        driver = conftest.driver

        # Locate the username input field by its ID and store it in a variable.
        username = driver.find_element(By.ID, "user-name")

        # Enter the username into the input field.
        username.send_keys("standard_user")

        # Pause execution to allow time for entering the username.
        time.sleep(2)

        # Locate the password input field by its ID and store it in a variable.
        password = driver.find_element(By.ID, "password")

        # Enter the password into the input field.
        password.send_keys("secret_sauce")

        # Pause execution to allow time for entering the password.
        time.sleep(2)

        # Locate the login button by its ID and store it in a variable.
        login_button = driver.find_element(By.ID, "login-button")

        # Click on the login button to submit the credentials and log in.
        login_button.click()

        # Pause execution to allow time for the login process to complete.
        time.sleep(2)

        # Navigate to the product page for "Sauce Labs Backpack" and click on it.
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()

        # Pause to observe the product page.
        time.sleep(2)

        # Add the selected item to the cart.
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Pause to confirm the item was added.
        time.sleep(2)

        # Navigate to the cart to view the selected items.
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

        # Pause to observe items in the cart.
        time.sleep(2)

        # Assert that the "Sauce Labs Backpack" is correctly displayed in the cart.
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name'"
                                             "and text()='Sauce Labs Backpack']").is_displayed()

        # Click on "continue shopping" to return to the product list.
        driver.find_element(By.ID, "continue-shopping").click()

        # Pause before selecting another item.
        time.sleep(2)

        # Navigate to the product page for "Sauce Labs Bike Light" and click on it.
        driver.find_element(By.XPATH, "//*[@class='inventory_item_name ' and text()='Sauce Labs Bike Light']").click()

        # Pause to observe the product page.
        time.sleep(2)

        # Add the selected item to the cart.
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Pause to confirm the item was added.
        time.sleep(2)

        # Navigate back to the cart to view the selected items.
        driver.find_element(By.XPATH, "//*[@class='shopping_cart_link']").click()

        # Pause to observe items in the cart.
        time.sleep(2)

        # Assert that both "Sauce Labs Backpack" and "Sauce Labs Bike Light" are displayed in the cart.
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name'"
                                             "and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name'"
                                             "and text()='Sauce Labs Bike Light']").is_displayed()
