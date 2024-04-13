# Import the time module to use sleep function for pauses.
import time

# Import the WebDriver module from selenium to interact with web browsers.
from selenium import webdriver

# Set up the Edge browser using WebDriver.
driver = webdriver.Edge()

# Navigate to the website 'https://www.saucedemo.com/' using the browser.
driver.get("https://www.saucedemo.com/")

# Pause the execution for 2 seconds to allow the web page to load.
time.sleep(2)

# Maximize the browser window to ensure visibility of all elements.
driver.maximize_window()

# Pause execution to observe the maximized window.
time.sleep(2)

# Refresh the current page to reload its contents.
driver.refresh()

# Pause execution to observe changes post refresh.
time.sleep(2)

# Navigate to a new URL, in this case, Google's homepage.
driver.get("https://www.google.com/")

# Pause execution to allow the new page to load.
time.sleep(2)

# Navigate back to the previous page in the browser history.
driver.back()

# Pause execution to observe the page after navigating back.
time.sleep(2)

# Navigate forward in the browser history to the page visited before going back.
driver.forward()

# Pause execution to observe the page after navigating forward.
time.sleep(2)

# Minimize the browser window to see how the page looks in minimized form.
driver.minimize_window()

# Pause execution to observe the minimized window.
time.sleep(2)

# Open a new tab in the browser.
driver.switch_to.new_window("tab")

# Pause execution to observe the new tab.
time.sleep(2)

# Close the current tab or window.
driver.close()

# Pause execution to ensure the close operation completes.
time.sleep(2)

# Close the browser and end the session.
driver.quit()
