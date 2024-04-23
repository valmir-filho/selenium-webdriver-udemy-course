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

# Locate all elements that match the specified XPath and store them in a variable.
auth_fields = driver.find_elements(By.XPATH, "//*[@class = 'input_error form_input']")

# Print the number of located elements to verify how many match the criteria.
print(f"\nNumber of elements: {len(auth_fields)}.")

# Close the browser and end the session.
driver.quit()
