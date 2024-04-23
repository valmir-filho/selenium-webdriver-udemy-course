# Import the time module to use sleep function for pauses.
import time

# Import the WebDriver module from selenium to interact with web browsers.
from selenium import webdriver

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

# Print the title of the current page.
print(f"\nBrowser's title: {driver.title}.")

# Print the current URL of the browser.
print(f"\nCurrent browser's URL: {driver.current_url}")

# Print the source code of the current page.
print(f"\nBrowser's source code: {driver.page_source}")

# Close the browser and end the session.
driver.quit()
