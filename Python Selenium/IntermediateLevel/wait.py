import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# Chrome_driver - Chrome browser
# Impilicit wait is more like global timeout
x = 5
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(x)
# Impilicit wait = 5 seconds is the max timeout. If the element find in 2 seconds, it executes the flows
# Sleep = 2 seconds. If element found in 1 seconds, it will wait untill 2 seconds completes
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(x)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")  # lists[]
count = len(results)
print(count)
assert count > 0
# Chaining of web elements

for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)




