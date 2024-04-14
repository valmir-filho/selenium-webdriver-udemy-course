# Import the time module to use sleep function for pauses.
import time

# Import the WebDriver and By modules from selenium to interact with web browsers and locate elements.
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Edge browser using WebDriver.
driver = webdriver.Edge()

# Navigate to the website "https://www.saucedemo.com/" using the browser.
driver.get("https://www.saucedemo.com/")

# Pause the execution for 2 seconds to allow the web page to load.
time.sleep(2)

# Maximize the browser window to ensure visibility of all elements.
driver.maximize_window()

# Pause execution to observe the maximized window.
time.sleep(2)

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

# Locate the product title element by its XPath to confirm successful login and display.
products_title = driver.find_element(By.XPATH, "//span[@class='title']")

# Print the text of the products title element.
print(f"\nProducts title: {products_title.text}.")

# Locate the first backpack image element by its XPath and store it in a variable.
backpack_image = driver.find_element(By.XPATH, "(//img[@class='inventory_item_img'])[1]")

# Print the alt attribute of the first backpack image to verify its content.
print(f"\nAttribute: {backpack_image.get_attribute('alt')}.")

# Close the browser and end the session.
driver.quit()
