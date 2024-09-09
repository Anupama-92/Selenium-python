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
try:
    item = ["Sauce Labs Bolt T-Shirt","Sauce Labs Backpack"]
    print(type(item))
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product_element in products:
        product_name = product_element.find_element(By.CLASS_NAME, "inventory_item_name ").text
        if product_name == item[2]:
           print("Index value is out of range ")
except IndexError:
    print("Index value is out of range ")



# sleep(5)
# print("checking with cart items")
# cart=driver.find_element(By.CLASS_NAME, "shopping_cart_container")
# cart.click()
# sleep(5)
# # cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
# # if len(cart_items) != 1:
# #     for item in cart_items:
# #         item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
# #         # driver.execute_script("arguments[0].remove()", item)
# #         print(f"Removed {item_name} from cart")
# driver.find_element(By.ID, "checkout").click()
# sleep(5)
# driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Test")
# driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Test")
# driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("1234")
# driver.find_element(By.ID, "continue").click()
# sleep(5)
# driver.find_element(By.ID, "finish").click()
# sleep(5)
# message = driver.find_element(By.CLASS_NAME, "complete-header").text
# print(message)
# assert "Thank you for your order!" in message
# driver.find_element(By.ID, "back-to-products").click()
# sleep(5)
# message2 = "Automated successfully"
# print(message2)







