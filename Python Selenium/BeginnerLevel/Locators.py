from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome_driver - Chrome browser
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# ID, xpath, CSS selector, class name, name, linkText
#   xpath - //tagname[@attribute='value']
# CSS - tagname[attribute='value'], #id, .classname
driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.NAME, "login-button").click()
sleep(5)
driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
sleep(5)
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()
sleep(5)
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Test")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Test")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("1234")
driver.find_element(By.ID, "continue").click()
sleep(5)
driver.find_element(By.ID, "finish").click()
sleep(5)
message = driver.find_element(By.CLASS_NAME, "complete-header").text
print(message)
assert "Thank you for your order!" in message
driver.find_element(By.ID, "back-to-products").click()
sleep(5)
message2 = "Automated successfully"
print(message2)







