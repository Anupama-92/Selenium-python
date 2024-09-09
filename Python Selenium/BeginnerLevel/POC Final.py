from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome_driver - Chrome browser
x = 5
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# ID, xpath, CSS selector, class name, name, linkText
#   xpath - //tagname[@attribute='value']
# CSS - tagname[attribute='value'], #id, .classname
# driver.find_element(By.NAME, "user-name").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
driver.find_element(By.NAME, "password").send_keys("secret_sauce")
driver.find_element(By.NAME, "login-button").click()
sleep(x)
item = ["Sauce Labs Bolt T-Shirt","Sauce Labs Backpack"]


def productsList(product):
    products1 = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product_element in products1:
        product_name = product_element.find_element(By.CLASS_NAME, "inventory_item_name ").text
        if product_name == product[1]:
            addtocart = product_element.find_element(By.CLASS_NAME, "btn_primary")
            addtocart.click()
            break
        elif product_name == product[0]:
            addtocart1 = product_element.find_element(By.CLASS_NAME, "btn_primary")
            addtocart1.click()


productsList(item)
print(type(item))

sleep(x)
# print("checking with cart items")
cart = driver.find_element(By.CLASS_NAME, "shopping_cart_container")
cart.click()
sleep(x)
# cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
# if len(cart_items) != 1:
#     for item in cart_items:
#         item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
#         # driver.execute_script("arguments[0].remove()", item)
#         print(f"Removed {item_name} from cart")
driver.find_element(By.ID, "checkout").click()
sleep(x)
# page = input("What is page name?\n")
# print(page)
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Test")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Test")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("1234")
driver.find_element(By.ID, "continue").click()
sleep(x)
driver.find_element(By.ID, "finish").click()
sleep(x)
message = driver.find_element(By.CLASS_NAME, "complete-header").text
print(message)
page = input("What is the success message \n")
if page == message:
    print(page)
    sleep(x)
    driver.find_element(By.ID, "back-to-products").click()
    sleep(x)
    message2 = "Automated successfully"
    print(message2)
else:
    message3 = "Fail"
    print(message3)







