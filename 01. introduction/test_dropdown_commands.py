# Import the time module to use sleep function for pauses.
import time

# Import webdriver from selenium to control the browser, By to locate elements, and Select to interact with dropdown
# elements.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Set up the Edge browser using WebDriver.
driver = webdriver.Edge()

# Navigate to the specified website using the browser.
driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")

# Pause the execution for 2 seconds to allow the web page to load initially.
time.sleep(2)

# Maximize the browser window to ensure visibility of all elements.
driver.maximize_window()

# Pause execution briefly to observe the maximized window.
time.sleep(2)

# Set an implicit wait of 12 seconds to allow elements to load before interacting with them.
driver.implicitly_wait(12)

# Locate the dropdown for products and wrap it in a Select object for easier manipulation.
dropdown_products = Select(driver.find_element(By.XPATH, "//select[@id='first']"))

# Select the option "Google" by its visible text.
dropdown_products.select_by_visible_text("Google")

# Pause execution to observe the selection effect.
time.sleep(2)

# Locate the dropdown for animals and wrap it in a Select object.
dropdown_animals = Select(driver.find_element(By.XPATH, "//select[@id='animals']"))

# Select the option with the value attribute "babycat".
dropdown_animals.select_by_value("babycat")

# Pause execution to observe the selection effect.
time.sleep(2)

# Select the fourth item in the dropdown by its index (index starts at 0).
dropdown_animals.select_by_index(3)

# Pause execution to observe the selection effect.
time.sleep(2)

# Locate the dropdown for food items and wrap it in a Select object.
dropdown_food_items = Select(driver.find_element(By.XPATH, "//select[@id='second']"))

# Select the option "Pizza" by its visible text.
dropdown_food_items.select_by_visible_text("Pizza")

# Pause execution to observe the selection effect.
time.sleep(2)

# Select another option "Bonda" by its visible text.
dropdown_food_items.select_by_visible_text("Bonda")

# Pause execution to observe the selection effect.
time.sleep(2)

# Close the browser and end the session.
driver.quit()
