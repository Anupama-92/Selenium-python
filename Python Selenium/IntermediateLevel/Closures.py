from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def product_search(product):

    def cart():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        driver.find_element(By.NAME, "login-button").click()
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

    return cart


item = ["Sauce Labs Bolt T-Shirt", "Sauce Labs Backpack"]
cart_func = product_search(item)
cart_func()

