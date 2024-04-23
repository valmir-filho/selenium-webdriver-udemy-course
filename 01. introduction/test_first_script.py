# Import the time module to use sleep function for pauses.
import time

# Import the webDriver module from selenium to interact with web browsers.
from selenium import webdriver

# Set up the Edge browser using WebDriver.
driver = webdriver.Edge()

# Navigate to the website "https://www.saucedemo.com/" using the browser.
driver.get("https://www.saucedemo.com/")

# Pause the execution for 2 seconds to allow the web page to load.
time.sleep(2)
