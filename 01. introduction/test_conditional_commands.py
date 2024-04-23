# Import the time module to use sleep function for pauses.
import time

# Import the WebDriver and By modules from selenium to interact with web browsers and locate elements.
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Edge browser using WebDriver.
driver = webdriver.Edge()

# Navigate to the website "https://demo.applitools.com/" using the browser.
driver.get("https://demo.applitools.com/")

# Pause the execution for 2 seconds to allow the web page to load.
time.sleep(2)

# Maximize the browser window to ensure visibility of all elements.
driver.maximize_window()

# Pause execution to observe the maximized window.
time.sleep(2)

# Locate the username input field by its ID.
username = driver.find_element(By.ID, "username")

# Locate the remember me checkbox using its type attribute via XPath.
remember_checkbox = driver.find_element(By.XPATH, "//*[@type='checkbox']")

# Print the visibility status of the username input field.
print(f"\nIs the element being displayed? {username.is_displayed()}.")

# Print the enabled status of the username input field.
print(f"\nIs the element being enabled? {username.is_enabled()}.")

# Print the initial selection status of the remember me checkbox.
print(f"\nIs the element being selected? {remember_checkbox.is_selected()}.")

# Click the remember me checkbox to change its selection status.
remember_checkbox.click()

# Print the updated selection status of the remember me checkbox after clicking it.
print(f"\nIs the element being selected? {remember_checkbox.is_selected()}.")

# Close the browser and end the session.
driver.quit()
