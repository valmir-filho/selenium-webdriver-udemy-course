# Import the time module to use sleep function for pauses.
import time

# Import the WebDriver and By modules from selenium to interact with web browsers and locate elements.
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Edge browser using WebDriver.
driver = webdriver.Edge()

# Navigate to the specified website using the browser.
driver.get("https://chercher.tech/practice/implicit-wait-example")

# Pause the execution for 2 seconds to allow the web page to load initially.
time.sleep(2)

# Maximize the browser window to ensure visibility of all elements.
driver.maximize_window()

# Pause execution briefly to observe the maximized window.
time.sleep(2)

# Set an implicit wait of 12 seconds to allow elements to load before interacting with them.
driver.implicitly_wait(12)

# Locate the checkbox on the page by its XPath and store it in a variable.
checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")

# Assert that the checkbox is displayed on the page.
assert checkbox.is_displayed()

# Pause execution to observe the checkbox's state.
time.sleep(2)

# Close the browser and end the session.
driver.quit()
