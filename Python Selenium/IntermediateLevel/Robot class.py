from selenium import webdriver
import pyautogui
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.flipkart.com')
driver.maximize_window()

# Close the login popup using pyautogui
time.sleep(2)  # Wait for the popup to load
pyautogui.click(x=1295, y=310)  # Adjust the coordinates based on your screen resolution

# Find the search box and enter a product name
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('laptop')

# Trigger the search
search_box.submit()

# Wait for the search results to load
time.sleep(5)  # Adjust the wait time based on your internet speed

# Use pyautogui to scroll down to view more products
pyautogui.scroll(-500)  # Scroll down (positive values scroll up)

# Optionally, you can click on specific coordinates using pyautogui
# For example, clicking on the first product after scrolling
time.sleep(2)
pyautogui.click(x=200, y=500)  # Adjust the coordinates to click on the desired product

driver.quit()
