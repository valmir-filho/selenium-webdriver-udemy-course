# Import the time module to use sleep function for pauses.
import time

# Import the WebDriver and By modules from selenium to interact with web browsers and locate elements.
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Edge browser using WebDriver.
driver = webdriver.Edge()

# Navigate to the specified website using the browser.
driver.get("https://www.saucedemo.com/")

# Pause the execution for 2 seconds to allow the web page to load initially.
time.sleep(2)

# Maximize the browser window to ensure visibility of all elements.
driver.maximize_window()

# Pause execution briefly to observe the maximized window.
time.sleep(2)

# Set an implicit wait of 12 seconds to allow elements to load before interacting with them.
driver.implicitly_wait(12)

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

# Select the item "Sauce Labs Backpack" by clicking its name on the product list.
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

# Select the item "Sauce Labs Bike Light" by clicking its name on the product list.
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

# Assert that both the "Sauce Labs Backpack" and "Sauce Labs Bike Light" are displayed in the cart.
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name'"
                                     "and text()='Sauce Labs Backpack']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name'"
                                     "and text()='Sauce Labs Bike Light']").is_displayed()

# Proceed to checkout by clicking the checkout button.
driver.find_element(By.ID, "checkout").click()

# Pause to allow time for the checkout page to load.
time.sleep(2)

# Fill in the checkout form with user information.
driver.find_element(By.ID, "first-name").send_keys("Valmir")
driver.find_element(By.ID, "last-name").send_keys("Moro")
driver.find_element(By.ID, "postal-code").send_keys("82515965")

# Pause to ensure all information is entered.
time.sleep(2)

# Continue to the next step of the checkout process.
driver.find_element(By.ID, "continue").click()

# Pause to allow time for the next step to load.
time.sleep(2)

# Complete the checkout process by clicking the finish button.
driver.find_element(By.ID, "finish").click()

# Pause to ensure the process is completed.
time.sleep(2)

# Close the browser and end the session.
driver.quit()
